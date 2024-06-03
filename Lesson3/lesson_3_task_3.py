from Address import Address
from Mailing import Mailing

to_address = Address("601642", "Карабаново", "Мира", "10", "15")
from_address = Address("600015", "Владимир", "Чайковского", "44", "45")
mailing = Mailing(to_address, from_address, "ABC123", "5000")

print("Отправление", mailing.track, "из", mailing.from_address.index,
    mailing.from_address.gorod, mailing.from_address.ulica,
    mailing.from_address.dom, "-", mailing.from_address.kvartira,
    "в", mailing.to_address.index, mailing.to_address.gorod,
    mailing.to_address.ulica, mailing.to_address.dom, "-",
    mailing.to_address.kvartira, ". Стоимость", mailing.cost, "рублей.")
