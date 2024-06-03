class User:

    def __init__(self, first_name, last_name):
        self.username = first_name
        self.userfam = last_name

    def Name(self):
        print("Имя: ", self.username)

    def Fam(self):
        print("Фамилия: ", self.userfam)

    def NameFam(self):
        print("Имя и фамилия: ", self.username, self.userfam)


# Можно вот и таким образом дописать код и скрипт отработает из одного файла:)
#
# first_name = input("Как Ваше имя? ")
# last_name = input("Как Ваша фамилия? ")
#
# my_user = User(first_name, last_name)
#
# my_user.Name()
# my_user.Fam()
# my_user.NameFam()
