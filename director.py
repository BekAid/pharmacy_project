import csv
from abc import ABC, abstractmethod
import datetime
import calendar
from datetime import datetime



class Abstract(ABC):
    def __init__(self):
        pass

    def search_drug(self, drug_name):
        with open("drugs.csv", 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            print(" | ".join(map(str, headers)))

            for row in reader:
                row_drug_name = row[0]
                if row_drug_name == drug_name:
                    print(" | ".join(map(str, row)))

    def delete_person(self, first_name, last_name, file_name):
        keep_rows = []  # Список для хранения строк, которые нужно оставить
        with open(file_name, "r") as file:
            reader = csv.reader(file)

            for row in reader:
                row_first_name, row_last_name = row[:2]  # Предполагается, что имя и фамилия находятся в первых двух столбцах
                if row_first_name != first_name or row_last_name != last_name:
                    keep_rows.append(row)  # Записываем оставшиеся строки обратно в файл
                else:
                    print(first_name, last_name, "удален успешно!")

        with open(file_name, "w", newline='') as file_write:
            writer = csv.writer(file_write)
            writer.writerows(keep_rows)


class Director(Abstract):
    def __init__(self, director_name):
        super().__init__()
        self.director_name = director_name
    
    def search_drug(self, drug_name):
        super().search_drug(drug_name)

        choice = str(input("\n1)Find another drug\n2)Main menu\nChoice:"))
        if choice == "1":
            Director.search_drug(self, (input("Enter drug name:")).capitalize())
        elif choice == "2":
            Director.main_menu(self)

    def search_manager(self, name, surname):
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Читаем заголовки столбцов
            print('  |  '.join(map(str, headers)))

            for row in reader:
                row_first_name, row_last_name = row[
                                                :2]  # Предполагается, что имя и фамилия находятся в первых двух столбцах
                position = row[headers.index('Position')]

                if row_first_name == name and row_last_name == surname and position == "manager":
                    print(' | '.join(map(str, row)))
                    choice = str(input("\n1)Delete\n2)Edit info\n3)Find another seller\n4)Main menu\nChoice:"))
                    if choice == "1":
                        Director.delete_person(self, name, surname)
                    elif choice == "2":
                        Director.edit_manager(self, name, surname)
                    elif choice == '3':
                        Director.search_manager(self, (input("Enter name:")).capitalize(),
                                                (input("Enter surname:")).capitalize())
                    elif choice == '4':
                        Director.main_menu(self)
                    else:
                        print("you entered wrong num!bla bla bla")

            choice = str(input("\n1)Find another manager\n2)Main menu\nChoice:"))
            if choice == "1":
                Director.search_manager(self, (input("Enter name:")).capitalize(),
                                        (input("Enter surname:")).capitalize())
            elif choice == "2":
                Director.main_menu(self)

    def delete_person(self, name, surname, file="users.csv"):
        super().delete_person(name, surname, file)

    def edit_manager(self, name, surname):
        rows = []
        found = False
        with open('users.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == name and row['Surname'] == surname:
                    fields = ["Name", "Surname", "Age", "Position", "Login", "Password"]
                    change_field = input(f"{fields}\nEnter what you want to change:").capitalize()
                    if change_field in fields:
                        row[change_field] = input("for what?:")
                    else:
                        print('You entered wrong field')

                    found = True
                rows.append(row)
        fieldnames = ["Name", "Surname", "Age", "Position", "Login", "Password"]
        with open('users.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        choice = str(input("\n1)Find another seller\n2)Main menu\nChoice:"))
        if choice == "1":
            Director.search_manager(self, (input("Enter name:")).capitalize(), (input("Enter surname:")).capitalize())
        elif choice == "2":
            Director.main_menu(self)

    def search_customer(self, name, surname):
        with open("customers.csv", "r") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Читаем заголовки столбцов
            print('  |  '.join(map(str, headers)))

            for row in reader:
                row_first_name, row_last_name = row[
                                                :2]  # Предполагается, что имя и фамилия находятся в первых двух столбцах
                if row_first_name == name and row_last_name == surname:
                    print(' | '.join(map(str, row)))

            choice = str(input("\n1)Find another customer\n"
                               "2)Main menu\n"
                               "Choice:"))
            if choice == "1":
                Director.search_customer(self,
                                         (input("Enter name:")).capitalize(),
                                         (input("Enter surname:")).capitalize())
            elif choice == "2":
                Director.main_menu(self)

    def add_manager(self):
        name = input("Enter name:").capitalize()
        surname = input("Enter surname:").capitalize()
        age = input("Enter age:")
        position = 'manager'
        login = input("Think up login:")
        password = input("Think up password:")

        data = [name, surname, age, position, login, password]
        with open('users.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
            print("New manager registered successfully!")

        choice = str(input("\n1)Add another seller\n2)Main menu\nChoice:"))
        if choice == "1":
            Director.add_manager(self)
        elif choice == "2":
            Director.main_menu(self)

    def report(self, report_type):
        if report_type == '1':
            month = int(input("Enter number of month you want report get:"))
            with open("finaicies.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)

                date_index = headers.index("Time")
                price_index = headers.index("Price")

                count = 0
                for row in reader:
                    if datetime.strptime(row[date_index], '%d-%m-%Y %H:%M').month == month:
                        count += int(row[price_index])
                print(f"Your income for {calendar.month_name[month]} is {count} som")

        elif report_type == '2':
            read_or_write = input("Enter 1)read or 2)write:")
            
            if read_or_write == '1' or read_or_write == 'read':
                with open("report.txt", 'r') as txtfile:
                    for line in txtfile:
                        print(line, end="")

            elif read_or_write == '2' or read_or_write == 'write':
                message = self.director_name + ": " + str(input("Enter your message:"))
                now = datetime.now()
                
                with open("report.txt", 'a', newline="") as file:
                    file.writelines(f"\n{now.strftime('%d-%m-%Y %H:%M')}\n{message}\n")
        choice = str(input("\n1)Financial\n"
                           "2)Manager's\n"
                           "3)Main menu\n"
                           "Choice:"))
        if choice == "1":
            Director.report(self, '1')
        elif choice == '2':
            Director.report(self, "2")
        elif choice == "3":
            Director.main_menu(self)

    def main_menu(self):
        choice = str(input("1) Search drug\n"
                           "2) Search worker\n"
                           "3) Add manager\n"
                           "4) Search customer\n"
                           "5) Read reports\n"
                           "Please choose function:\n"))
        if choice == "1":
            Director.search_drug(self, (input("Enter drug name:")).capitalize())
        elif choice == '2':
            Director.search_manager(self, (input("Enter name:")).capitalize(), (input("Enter surname:")).capitalize())
        elif choice == '3':
            Director.add_manager(self)
        elif choice == '4':
            Director.search_customer(self, (input("Enter name:")).capitalize(), (input("Enter surname:")).capitalize())
        elif choice == '5':
            Director.report(self, input("1)financial or 2)manager report"))


# director_start = Director('Bekbol')
# director_start.main_menu()