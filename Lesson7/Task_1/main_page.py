from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.driver.maximize_window()

    # Заполнение формы с персональными данными
    def fill_form(self, first_name, last_name, address, email, phone,
                  zip_code, city, country, job_position, company):
        self.driver.find_element(By.NAME, "first-name").send_keys(first_name)
        self.driver.find_element(By.NAME, "last-name").send_keys(last_name)
        self.driver.find_element(By.NAME, "address").send_keys(address)
        self.driver.find_element(By.NAME, "e-mail").send_keys(email)
        self.driver.find_element(By.NAME, "phone").send_keys(phone)
        self.driver.find_element(By.NAME, "zip-code").send_keys(zip_code)
        self.driver.find_element(By.NAME, "city").send_keys(city)
        self.driver.find_element(By.NAME, "country").send_keys(country)
        self.driver.find_element(By.NAME, "job-position").send_keys(
            job_position)
        self.driver.find_element(By.NAME, "company").send_keys(company)

    def get_element_by_class(self, class_name):
        element = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        return element

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, "button.btn").click()
