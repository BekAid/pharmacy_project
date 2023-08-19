import csv
import datetime
import calendar
from datetime import datetime, date

from director import Abstract

class Manager(Abstract):

    def __init__(self, manager_name):
        super().__init__()
        self.manager_name = manager_name


    def search_drug(self, drug_name):
        super().search_drug(drug_name)

        choice = str(input("\n1)Find another drug\n2)Main menu\nChoice:"))
        if choice == "1":
            Manager.search_drug(self, (input("Enter drug name:")).capitalize())
        elif choice == "2":
            Manager.main_menu(self)

    def search_seller(self, name, surname):
        with open("users.csv", "r") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Читаем заголовки столбцов
            print('  |  '.join(map(str, headers)))


            for row in reader:
                row_first_name, row_last_name = row[:2] # Предполагается, что имя и фамилия находятся в первых двух столбцах
                position = row[headers.index('Position')]

                if row_first_name == name and row_last_name == surname and position == "seller":
                    print(' | '.join(map(str, row)))
                    choice = str(input("\n1)Delete\n2)Edit info\n3)Find another seller\n4)Main menu\nChoice:"))
                    if choice == "1":
                        Manager.delete_person(self, name, surname)
                    elif choice == "2":
                        Manager.edit_seller(self, name, surname)
                    elif choice == '3':
                        Manager.search_seller(self, (input("Enter name:")).capitalize(), (input("Enter surname:")).capitalize())
                    elif choice == '4':
                        Manager.main_menu(self)
                    else:
                        print("you entered wrong num!bla bla bla")

            choice = str(input("\n1)Find another seller\n2)Main menu\nChoice:"))
            if choice == "1":
                Manager.search_seller(self, (input("Enter name:")).capitalize(),(input("Enter surname:")).capitalize())
            elif choice == "2":
                Manager.main_menu(self)

    def delete_person(self, name, surname, file = "users.csv"):
        super().delete_person(name, surname, file)

    def edit_seller(self, name, surname):
        rows = []
        found = False
        with open('users.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == name and row['Surname'] == surname:
                    fields = ["Name","Surname","Age","Position","Login","Password"]
                    change_field = input(f"{fields}\nEnter what you want to change:").capitalize()
                    if change_field in fields:
                        row[change_field] = input("for what?:")
                    else:
                        print('You entered wrong field')

                    found = True
                rows.append(row)
        fieldnames = ["Name", "Surname", "Age", "Position", "Login", "Password"]
        with open('users.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        choice = str(input("\n1)Find another seller\n2)Main menu\nChoice:"))
        if choice == "1":
            Manager.search_seller(self, (input("Enter name:")).capitalize(), (input("Enter surname:")).capitalize())
        elif choice == "2":
            Manager.main_menu(self)

    def add_drug(self):
        new_or_not = str(input("\n1)Add new drug\n2)Restock\nChoice:"))
        if new_or_not == "1":
            name = input("Enter name:").capitalize()
            expiration = input("Enter expiration(year):")
            drug_type = input("Enter type(таблетки, жидкость):")
            heals = input('Enter heals from:')
            quantity = input('Enter quantity:')
            price = input('Enter price:')
            drug_id = input('Enter id')

            data = [name, expiration, drug_type, heals, quantity, price, date.today(), drug_id]
            with open('drugs.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(data)
                print("New drug registered successfully!")

        elif new_or_not == "2":
            drug_id = input('Enter id')
            quantity = input('Enter restock quantity:')
            money = input('How much was spend?:')
            rows = []
            found = False
            with open('drugs.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['ID'] == drug_id:
                        now = datetime.now()
                        row['Quantity'] = int(row['Quantity'])+ int(quantity)
                        row['Last replenishment'] = now.strftime('%d-%m-%Y')
                        found = True
                        data = [row['Name'], row['Type'], int(quantity)*-1, now.strftime('%d-%m-%Y %H:%M'),
                                int(money)*-1]
                        with open('finaicies.csv', 'a',newline='') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(data)
                    rows.append(row)

            fieldnames = ['Name','Expiration','Type','Heals from','Quantity','Price','Last replenishment','ID']
            with open('drugs.csv', 'w', newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(rows)
            print('База данных успешно обновлена!')



        choice = str(input("\n1)Add another drug\n2)Main menu\nChoice:"))
        if choice == "1":
            Manager.add_drug(self)
        elif choice == "2":
            Manager.main_menu(self)

    def add_seller(self):
        name = input("Enter name:").capitalize()
        surname = input("Enter surname:").capitalize()
        age = input("Enter age:")
        position = 'seller'
        login = input("Think up login:")
        password = input("Think up password:")

        data = [name, surname, age, position, login, password]
        with open('users.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
            print("New seller registered successfully!")

        choice = str(input("\n1)Add another seller\n2)Main menu\nChoice:"))
        if choice == "1":
            Manager.add_seller(self)
        elif choice == "2":
            Manager.main_menu(self)

    def read_messages(self, read_or_write):

        if read_or_write == '1' or read_or_write == 'read':
            with open("message.txt", 'r') as txtfile:
                for line in txtfile:
                    print(line, end="")

        elif read_or_write == '2' or read_or_write == 'write':
            message = self.manager_name + ": " + str(input("Enter your message:"))
            now = datetime.now()
            with open("message.txt", 'a', newline="") as file:
                writer = file.writelines(f"\n{now.strftime('%d-%m-%Y %H:%M')}\n{message}\n")

        choice = str(input("\n1)Read message\n"
                           "2)Send messages\n"
                           "3)Main menu\n"
                           "Choice:"))
        if choice == "1":
            Manager.read_messages(self, '1')
        elif choice == '2':
            Manager.read_messages(self, "2")
        elif choice == "3":
            Manager.main_menu(self)

    def report(self, read_or_write):

        if read_or_write == '1' or read_or_write == 'read':
            with open("report.txt", 'r') as txtfile:
                for line in txtfile:
                    print(line, end="")

        elif read_or_write == '2' or read_or_write == 'write':
            monthly_message = input("Enter 1)monthly or 2)message:")
            if monthly_message =="1":
                manager.monthly_report()

            elif monthly_message == '2':
                message = self.manager_name + ": " + str(input("Enter your message:"))
                now = datetime.now()
                with open("report.txt", 'a', newline="") as file:
                    writer = file.writelines(f"\n{now.strftime('%d-%m-%Y %H:%M')}\n{message}\n")


        choice = str(input("\n1)Read message\n"
                           "2)Send report or messages\n"
                           "3)Main menu\n"
                           "Choice:"))
        if choice == "1":
            Manager.report(self, '1')
        elif choice == '2':
            Manager.report(self, "2")
        elif choice == "3":
            Manager.main_menu(self)
    def monthly_report(self):
        with open('finaicies.csv', 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            sold_drugs = {}
            bought_drugs = {}

            name_index = headers.index('Name')
            quantity_index = headers.index('Quantity')
            price_index = headers.index('Price')
            date_index = headers.index("Time")

            count = 0
            current_month = datetime.now().month
            for row in reader:
                if datetime.strptime(row[date_index], '%d-%m-%Y %H:%M').month == current_month:
                    count += int(row[price_index])
                    if int(row[quantity_index]) >= 0:
                        if row[name_index] not in sold_drugs:
                            sold_drugs[row[name_index]] = row[quantity_index]

                        else:
                            sold_drugs[row[name_index]] = int(sold_drugs.get(row[name_index])) + int(row[quantity_index])
                    else:
                        if row[name_index] not in bought_drugs:
                            bought_drugs[row[name_index]] = abs(int(row[quantity_index]))

                        else:
                            bought_drugs[row[name_index]] = abs(int(bought_drugs.get(row[name_index])) + int(
                                row[quantity_index]))
            now = datetime.now()
            with open("report.txt", 'a', newline="") as file:
                file.writelines(f"\n{now.strftime('%d-%m-%Y %H:%M')}\n{self.manager_name}:\n")
                for key in sold_drugs:
                    value = sold_drugs[key]
                    file.writelines(f"Лекартсво: {key}, Продано: {value} штук за этот месяц\n")
                for key in bought_drugs:
                    value = bought_drugs[key]
                    file.writelines(f"Лекартсво: {key}, Куплено: {value} штук за этот месяц\n")
                file.writelines(f"Your income for {calendar.month_name[current_month]} is {count} som\n")



    def financies(self):
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
        choice = str(input("\n1)Get another report\n2)Main menu\nChoice:"))
        if choice == "1":
            Manager.financies(self)
        elif choice == "2":
            Manager.main_menu(self)


    def main_menu(self):
        choice = str(input("1) Search drug\n"
                           "2) Search seller\n"
                           "3) Add drug\n"
                           "4) Add seller\n"
                           "5) Read messages\n"
                           "6) Send report to director\n"
                           "7) See financial report\n"
                           "Please choose function:"))
        if choice == "1":
            Manager.search_drug(self, (input("Enter drug name:")).capitalize())
        elif choice == '2':
            Manager.search_seller(self, (input("Enter name:")).capitalize(), (input("Enter surname:")).capitalize())
        elif choice == '3':
            Manager.add_drug(self)
        elif choice == '4':
            Manager.add_seller(self)
        elif choice == '5':
            Manager.read_messages(self, input("Enter 1)read or 2)write:"))
        elif choice == "6":
            Manager.report(self, input("Enter 1)read or 2)write:"))
        elif choice == '7':
            Manager.financies(self)


# manager = Manager('Jazgul')
# manager.main_menu()

