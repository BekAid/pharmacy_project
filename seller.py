import csv
import datetime
from datetime import datetime, date


from director import Abstract


class Seller(Abstract):

    def __init__(self, seller_name):
        super().__init__()
        self.seller_name = seller_name

    def search_drug(self, drug_name):
        super().search_drug(drug_name)

        choice = str(input("\n1)Find another drug\n2)Main menu\nChoice:"))
        if choice == "1":
            Seller.search_drug(self, (input("Enter drug name:")).capitalize())
        elif choice == "2":
            Seller.main_menu(self)

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
                    choice = str(input("\n1)Delete customer\n"
                                       "2)Edit info\n"
                                       "3)Find another customer\n"
                                       "4)Main menu\n"
                                       "Choice:"))
                    if choice == "1":
                        Seller.delete_person(self, name, surname)
                    elif choice == "2":
                        Seller.edit_customer(self, name, surname)
                    elif choice == '3':
                        Seller.search_customer(self,
                                               (input("Enter name:")).capitalize(),
                                               (input("Enter surname:")).capitalize())
                    elif choice == '4':
                        Seller.main_menu(self)
                    else:
                        print("you entered wrong num!bla bla bla")

            choice = str(input("\n1)Find another customer\n"
                               "2)Main menu\n"
                               "Choice:"))
            if choice == "1":
                Seller.search_customer(self,
                                       (input("Enter name:")).capitalize(),
                                       (input("Enter surname:")).capitalize())
            elif choice == "2":
                Seller.main_menu(self)

    def delete_person(self, first_name, last_name, file_name="customers.csv"):
        super().delete_person(first_name, last_name, file_name)

    def add_customer(self):
        name = input("Enter name:").capitalize()
        surname = input("Enter surname:").capitalize()
        age = input("Enter age:")
        phone = input('Enter phone number(+996...):')

        data = [name, surname, age, phone]
        with open('customers.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
            print("New customer registered successfully!")

        choice = str(input("\n1)Add another customer\n"
                           "2)Main menu\n"
                           "Choice:"))
        if choice == "1":
            Seller.add_customer(self)
        elif choice == "2":
            Seller.main_menu(self)

    def edit_customer(self, name, surname):
        rows = []
        found = False
        with open('customers.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Name'] == name and row['Surname'] == surname:
                    fields = ["Name", "Surname", "Age", "Phone"]
                    change_field = input(f"{fields}\nEnter what you want to change:").capitalize()
                    if change_field in fields:
                        row[change_field] = input("for what?:")
                    else:
                        print('You entered wrong field')

                    found = True
                rows.append(row)
        fieldnames = ["Name", "Surname", "Age", "Phone"]
        with open('customers.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        choice = str(input("\n1)Find another customer\n2)Main menu\nChoice:"))
        if choice == "1":
            Seller.search_customer(self, (input("Enter name:")).capitalize(), (input("Enter surname:")).capitalize())
        elif choice == "2":
            Seller.main_menu(self)

    def message(self, read_or_write):

        if read_or_write == '1' or read_or_write == 'read':
            with open("message.txt", 'r') as txtfile:
                for line in txtfile:
                    print(line, end="")

        elif read_or_write == '2' or read_or_write == 'write':
            message = self.seller_name + ": " + str(input("Enter your message:"))
            now = datetime.now()
            with open("message.txt", 'a', newline="") as file:
                writer = file.writelines(f"\n{now.strftime('%d-%m-%Y %H:%M')}\n{message}\n")

        choice = str(input("\n1)Read message\n"
                           "2)Send messages\n"
                           "3)Main menu\n"
                           "Choice:"))
        if choice == "1":
            Seller.message(self, '1')
        elif choice == '2':
            Seller.message(self, "2")
        elif choice == "3":
            Seller.main_menu(self)

    def buy_drug(self):
        finaicies_rows = []
        drugs_rows = []
        bool = True
        while bool:

            id = input("Введите id")
            number = int(input("Введите количество:"))
            for i in range(10):
                print(" " * 100)

            print("Name | Type | Quantity | Price")

            with open("drugs.csv", "r", newline='') as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)



                name_index = headers.index('Name')
                type_index = headers.index('Type')
                quantity_index = headers.index('Quantity')
                price_index = headers.index('Price')
                id_index = headers.index("ID")

                for row in reader:
                    if row[id_index] == str(id):
                        now = datetime.datetime.now()
                        row[quantity_index] = int(row[quantity_index]) - number
                        data = [row[name_index], row[type_index], number, now.strftime('%d-%m-%Y %H:%M'), int(row[price_index])*number]
                        # Добавляем элементы из другого итерируемого объекта (например, другого списка)
                        finaicies_rows.extend(data)
                        all_price = 0
                        for k in range(0, len(finaicies_rows), 5):
                            print(finaicies_rows[k], finaicies_rows[k + 1], finaicies_rows[k + 2], finaicies_rows[k + 4])
                            all_price += finaicies_rows[k + 4]
                        print(f"Итог: {all_price} сом")

                        answer1 = input("Добавить лекартсво? 1) Да 2) Нет")
                        if answer1 == "1":
                            csvfile.seek(0)
                            drugs_rows.clear()
                            break

                        elif answer1 == '2':
                            answer2 = input("Оплата совершена? 1) Да 2) Нет")
                            if answer2 == '1':
                                for k in range(0, len(finaicies_rows), 5):
                                    list_csv = [finaicies_rows[k], finaicies_rows[k + 1], finaicies_rows[k + 2], finaicies_rows[k + 3], finaicies_rows[k + 4]]
                                    with open('finaicies.csv', 'a', newline='') as csvfile2:
                                        writer = csv.writer(csvfile2)
                                        writer.writerow(list_csv)

                            else:
                                bool = False

                    drugs_rows.append(row)

            # fieldnames = ['Name', 'Expiration', 'Type', 'Heals from', 'Quantity', 'Price', 'Last replenishment','ID']
            with open('drugs.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(drugs_rows)
                bool = False

        Seller.main_menu(self)

    def main_menu(self):
        choice = str(input("1) Search drug\n"
                           "2) Search client\n"
                           "3) Add client\n"
                           "4) Send message to manager\n"
                           "5) Buy drug\n"
                           "Please choose function:"))
        if choice == "1":
            Seller.search_drug(self, (input("Enter drug name:")).capitalize())
        elif choice == '2':
            Seller.search_customer(self, (input("Enter name:")).capitalize(), (input("Enter surname:")).capitalize())
        elif choice == '3':
            Seller.add_customer(self)
        elif choice == '4':
            Seller.message(self, input("Enter 1)read or 2)write:"))
        elif choice == '5':
            Seller.buy_drug(self)

# sel = Seller('Nargiza')
# sel.main_menu()
# sel.search_customer("Bekbol", "Aidarbekov")
# sel.search_drug("Парацетомол")
# sel.choice()

#посмотри покупку лекарств
#посмотри при покупке списывание с базы данных лекарств
