from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Хуавэй", "Хонор", "+79066153110")
phone2 = Smartphone("Нокиа", "2110", "+79051403357")
phone3 = Smartphone("Самсунг", "Galaxy", "+79051403356")
phone4 = Smartphone("Филипс", "strong", "+79267778899")
phone5 = Smartphone("LG", "Раскладушка", "+79103054433")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(phone.marka, "-", phone.model, ".", phone.telefon)
