import csv

from director import Director
from seller import Seller
from manager import Manager



class Registration:
    def __init__(self):
        pass

    def registration(self):
        global password
        name = input("Enter name:")
        surname = input("Enter surname:")
        age = input("Enter age:")
        login = input("think up a login:")

        while True:
            password1 = input("think up a password:")
            password2 = input("repeat password:")
            if password1 == password2:
                password = password1
                break
            else:
                print("passwords are not same, please repeat.")
                continue

        data = [name, surname, age, login, password]
        with open('users.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
        print("You registered successfully!")


class Login:

    def __init__(self):
        pass

    def authentificator(self):
        authenticated = True
        with open('users.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Читаем заголовки столбцов

            # Определяем индексы столбцов с логинами и паролями
            username_index = headers.index('Login')
            password_index = headers.index('Password')
            position_index = headers.index('Position')
            name_index = headers.index('Name')

            while authenticated:
                login = input("Введите логин: ")
                password = input("Введите пароль: ")

                for row in reader:
                    if row[username_index] == login and row[password_index] == password:
                        authenticated = False  # Логин и пароль найдены
                        print(f"Добро пожаловать {row[name_index]}")
                        if row[position_index] == "seller":
                            seller = Seller(row[name_index])
                            seller.main_menu()
                        elif row[position_index] == "manager":
                            manager = Manager(row[name_index])
                            manager.main_menu()
                        elif row[position_index] == 'director':
                            director = Director(row[name_index])
                            director.main_menu()

                print("Логин или пароль неверны, пожалуйста повторите попытку.")
                csvfile.seek(0)


# reg1 = Registration()
# reg1.registration()
# log1 = Login()
# log1.authentificator()
