import pytest
from empl import Company


api = Company("https://x-clients-be.onrender.com")


def test_get_list_of_employees():
    name = "SkyPro"
    descr = "курсы"
    company = api.create_company(name, descr)
    new_id = company["id"]
    employee_list = api.get_list_employee(new_id)
    assert len(employee_list) == 0


def test_add_new_employee():
    name = "SkyPro"
    descr = "курсы"
    company = api.create_company(name, descr)
    new_id = company["id"]

    new_employee = api.add_new_employee(new_id, "Antonio", "Rudy")
    assert new_employee["id"] > 0

    resp = api.get_list_employee(new_id)
    assert resp[0]["companyId"] == new_id
    assert resp[0]["firstName"] == "Antonio"
    assert resp[0]["isActive"] == True
    assert resp[0]["lastName"] == "Rudy"


def test_get_employee_by_id():
    name = "SkyPro"
    descr = "курсы"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Antonio", "Rudy")
    id_employee = new_employee["id"]
    get_info = api.get_employee_by_id(id_employee)
    assert get_info["firstName"] == "Antonio"
    assert get_info["lastName"] == "Rudy"


def test_change_employee_info():
    name = "SkyPro"
    descr = "курсы"
    company = api.create_company(name, descr)
    new_id = company["id"]
    new_employee = api.add_new_employee(new_id, "Antonio", "Rudy1")
    id_employee = new_employee["id"]

    update = api.update_employee_info(id_employee, "Rudy2", "tosha.rudanov@yandex.ru")
    assert update["id"] == id_employee
    assert update["email"] == "tosha.rudanov@yandex.ru"
    assert update["isActive"] == True
