import sqlite3
import sqlite3 as sql
import csv
from openpyxl import Workbook

car_info_list = ["ID", "Brand", "Model", "Kilometer", "Age", "Wrecked", "Purchase Price"]
car_adding_info = ("\nEntry must be exactly in this format:\n"
                               "brand,model,kilometer,age,wrecked(True or False),purchase_price(TL), 7- Exit")
searching_categories = "1- Brand\n2- Model\n3- Kilometer (for example 50.000 (shows the cars which lower than 50.000))\n4- Age (for example 5 (shows the cars which younger than 5))\n5- Wrecked (True or False)\n6- Purchase Price (for example 50.000 (shows the cars which cheaper than 50.000))\n7- Exit"
updating_categories = "1- Brand\n2- Model\n3- Kilometer\n4- Age\n5- Wrecked\n6- Purchase Price\n7- Exit"


class Car:
    db = sql.connect("/Users/huseyinozen/Desktop/Python Bootcamp/AutoGalleryManager/AutoGalleryDB.db")
    cursor = db.cursor()

    def __init__(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cars (id INTEGER PRIMARY KEY AUTOINCREMENT,brand TEXT, model TEXT, kilometer INTEGER, age INTEGER, wrecked BOOLEAN, purchase_price INTEGER)")

    def add_car(self):
        while True:
            print(car_adding_info)
            user_input = input("Enter car info: ")
            if user_input == "7":
                break
            car_info = tuple(user_input.split(","))
            try:
                kilometer = float(car_info[2])
                if not (0 < kilometer < 10000000):
                    raise ValueError("Kilometer must be between 0 and 10,000,000")

                age = int(car_info[3])
                if age < 0:
                    raise ValueError("Age must be a positive integer")

                wrecked = car_info[4].strip().lower()
                if wrecked not in ["true", "false"]:
                    raise ValueError("Wrecked info must be True or False")

                wrecked = wrecked == 'true'

                purchase_price = float(car_info[5])
                if purchase_price < 0:
                    raise ValueError("Purchase price must be a positive number")

                self.cursor.execute(
                    "INSERT INTO cars(brand, model, kilometer, age, wrecked, purchase_price) VALUES(?, ?, ?, ?, ?, ?)",
                    (car_info[0].strip(), car_info[1].strip(), kilometer, age, wrecked, purchase_price))
                self.db.commit()
                print("\nCar has been added to the database!\n")
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please try again.")
            except Exception as e:
                print(f"An error occurred: {e}")
                break

    def search_car(self):
        while True:
            print(searching_categories)
            category_input = input("Selection: ")
            if category_input == "7":
                break
            elif category_input == "1":
                brand_input = input("Enter brand name: ")
                try:
                    sql_query = f"SELECT * FROM cars WHERE brand='{brand_input}'"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        print("*" * 110)
                        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*car_info_list))
                        for row in result:
                            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))
                        print("*" * 110)
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "2":
                model_input = input("Enter model name: ")
                try:
                    sql_query = f"SELECT * FROM cars WHERE model='{model_input}'"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        print("*" * 110)
                        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*car_info_list))
                        for row in result:
                            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))
                        print("*" * 110)
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "3":
                kilometer_input = input("Enter max kilometer: ")
                try:
                    sql_query = f"SELECT * FROM cars WHERE kilometer<='{kilometer_input}'"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        print("*" * 110)
                        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*car_info_list))
                        for row in result:
                            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))
                        print("*" * 110)
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "4":
                age_input = input("Enter max age: ")
                try:
                    sql_query = f"SELECT * FROM cars WHERE age<='{age_input}'"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        print("*" * 110)
                        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*car_info_list))
                        for row in result:
                            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))
                        print("*" * 110)
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "5":
                wrecked_input = input("Enter wrecked info (1 for True, 0 for False): ")
                try:
                    if wrecked_input in ["0", "1"]:
                        sql_query = f"SELECT * FROM cars WHERE wrecked='{wrecked_input}'"
                        self.cursor.execute(sql_query)
                        result = self.cursor.fetchall()
                        if len(result) != 0:
                            print("*" * 110)
                            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*car_info_list))
                            for row in result:
                                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))
                            print("*" * 110)
                        else:
                            print("No results.")
                    else:
                        print("Wrong input!!! Enter '1' for True, '0' for False.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "6":
                purchase_price = input("Enter max purchase price: ")
                try:
                    sql_query = f"SELECT * FROM cars WHERE purchase_price<='{purchase_price}'"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        print("*" * 110)
                        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*car_info_list))
                        for row in result:
                            print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))
                        print("*" * 110)
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

    def print_all_cars(self):
        try:
            self.cursor.execute("SELECT * FROM cars")
            result = self.cursor.fetchall()
            if len(result) != 0:
                print("*" * 110)
                print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*car_info_list))
                for row in result:
                    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*row))
                print("*" * 110)
            else:
                print("No results.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def delete_car(self):
        while True:
            choice = input("Do you want to all data or specific car data? (all for deleting all, s for specific): ")

            if choice == "all":
                sure = input("Are you sure want to delete all car data? (y for YES, n for NO")
                if sure == "y":
                    try:
                        self.cursor.execute("DELETE FROM cars")
                        self.db.commit()
                        print("All car data have been deleted!")
                        break
                    except  Exception as e:
                        print("Something went wrong!", e)
                else:
                    print("Data not deleted.")
                    break

            elif choice == "s":
                print("Entry must be exactly in this format:\nbrand,model,kilometer")
                user_input = input("Enter: ")
                try:
                    car_info = tuple(user_input.split(","))
                    sql_query = f"DELETE FROM cars WHERE brand='{car_info[0]}' AND model='{car_info[1]}' AND kilometer='{car_info[2]}'"
                    self.cursor.execute(sql_query)
                    self.db.commit()
                    print("Car data has been deleted.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")
            else:
                print("Wrong input, enter 'all' or 's' !!!")

    def delete_all_sales_data(self):
        sure = input("Are you sure want to delete all sales data? (y for YES, n for NO): ")
        if sure == "y":
            try:
                self.cursor.execute("DELETE FROM sales")
                self.db.commit()
                print("All sales data have been deleted.")
            except Exception as e:
                print("Something went wrong!", e)
        else:
            print("Data not deleted.")

    def update_car(self):
        while True:
            car_id = input("Enter car index that will be updated: ")
            print(updating_categories)
            category_input = input("Selection: ")

            if category_input == "7":
                break

            elif category_input == "1":
                try:
                    sql_query = f"SELECT * FROM cars WHERE id={car_id}"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        new_brand_name = input("Enter new brand name: ")
                        self.cursor.execute(f"UPDATE cars SET brand='{new_brand_name}' WHERE id='{car_id}'")
                        self.db.commit()
                        print("Car info has been updated.")
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "2":
                try:
                    sql_query = f"SELECT * FROM cars WHERE id='{car_id}'"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        new_model_name = input("Enter new model name: ")
                        self.cursor.execute(f"UPDATE cars SET model='{new_model_name}' WHERE id='{car_id}'")
                        self.db.commit()
                        print("Car info has been updated.")
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "3":
                try:
                    sql_query = f"SELECT * FROM cars WHERE id='{car_id}'"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        new_kilometer = input("Enter new kilometer: ")
                        self.cursor.execute(f"UPDATE cars SET kilometer='{new_kilometer}' WHERE id='{car_id}'")
                        self.db.commit()
                        print("Car info has been updated.")
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "4":
                try:
                    sql_query = f"SELECT * FROM cars WHERE id='{car_id}'"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        new_age = input("Enter new age: ")
                        self.cursor.execute(f"UPDATE cars SET kilometer='{new_age}' WHERE id='{car_id}'")
                        self.db.commit()
                        print("Car info has been updated.")
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "5":
                try:
                    sql_query = f"SELECT * FROM cars WHERE id='{car_id}'"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        new_wrecked = input("Enter new wrecked info (1 for True, 0 for False): ")
                        if new_wrecked in ["0", "1"]:
                            self.cursor.execute(f"UPDATE cars SET wrecked='{new_wrecked}' WHERE id='{car_id}'")
                            self.db.commit()
                            print("Car info has been updated.")
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

            elif category_input == "6":
                try:
                    sql_query = f"SELECT * FROM cars WHERE id={car_id}"
                    self.cursor.execute(sql_query)
                    result = self.cursor.fetchall()
                    if len(result) != 0:
                        new_purchase_price = input("Enter new purchase price: ")
                        self.cursor.execute(f"UPDATE cars SET purchase_price='{new_purchase_price}' WHERE id='{car_id}'")
                        self.db.commit()
                        print("Car info has been updated.")
                    else:
                        print("No results.")
                    break
                except ValueError as ve:
                    print(f"Invalid input: {ve}. Please try again.")

    def write_db_to_csv(self):
        try:
            self.cursor.execute("SELECT * FROM cars")
            rows = self.cursor.fetchall()
            csv_file = "cars_data.csv"
            with open(csv_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["id", "brand", "model", "kilometer", "age", "wrecked", "purchase_price"])
                writer.writerows(rows)
            print(f'Data has been written to {csv_file}')
        except Exception as e:
            print("Something went wrong!", e)

    def write_db_to_xlsx(self):
        try:
            self.cursor.execute("SELECT * FROM cars")
            rows = self.cursor.fetchall()
            wb = Workbook()
            ws = wb.active
            ws.title = "Cars Data"
            ws.append(["id", "brand", "model", "kilometer", "age", "wrecked", "purchase_price"])
            for row in rows:
                ws.append(row)
            xlsx_file = "cars_data.xlsx"
            wb.save(xlsx_file)
            print(f'Data has been written to {xlsx_file}')
        except Exception as e:
            print("Something went wrong!", e)

    def sell_car(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY AUTOINCREMENT,brand TEXT, model TEXT, kilometer INTEGER, age INTEGER, wrecked BOOLEAN, purchase_price INTEGER, sale_price INTEGER, profit INTEGER)")
        while True:
            try:
                id_sale_price_input = input("Enter the id of the car sold and the sale price (exp: 5,40000): ").split(",")
                id_of_sold_car = id_sale_price_input[0]
                sale_price = int(id_sale_price_input[1])

                sql_query = f"SELECT * FROM cars WHERE id='{id_of_sold_car}'"
                self.cursor.execute(sql_query)
                result = self.cursor.fetchall()
                purchase_price = int(result[0][6]) # Getting purchase price
                profit = sale_price - purchase_price
                sql_query2 = f"INSERT INTO sales (brand, model, kilometer, age, wrecked, purchase_price, sale_price, profit) VALUES(?, ?, ?, ?, ?, ?, ?, ?)"
                parameters = list(result[0][1:])
                parameters.append(sale_price)
                parameters.append(profit)
                tuple_parameters = tuple(parameters)
                self.cursor.execute(sql_query2, tuple_parameters)
                self.cursor.execute(f"DELETE FROM cars WHERE id='{id_of_sold_car}'")
                self.db.commit()
                break
            except ValueError as ve:
                print(f"Invalid input: {ve}. Please try again.")

    def write_sales_to_csv(self):
        try:
            self.cursor.execute("SELECT * FROM sales")
            rows = self.cursor.fetchall()
            csv_file = "sales_data.csv"
            with open(csv_file, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["id", "brand", "model", "kilometer", "age", "wrecked", "purchase_price", "sale_price", "profit"])
                writer.writerows(rows)
            print(f"Sales data has been written to {csv_file}")
        except Exception as e:
            print("Something went wrong!", e)

    def write_sales_to_xlsx(self):
        try:
            self.cursor.execute("SELECT * FROM sales")
            rows = self.cursor.fetchall()
            wb = Workbook()
            ws = wb.active
            ws.title = "Sales Data"
            ws.append(["id", "brand", "model", "kilometer", "age", "wrecked", "purchase_price", "sale_price", "profit"])
            for row in rows:
                ws.append(row)
            xlsx_file = "sales_data.xlsx"
            wb.save(xlsx_file)
            print(f'Data has been written to {xlsx_file}')
        except Exception as e:
            print("Something went wrong!", e)

    def import_csv_to_sqlite(self):
        try:
            csv_input = input("Enter csv file's path: ")
            with open(csv_input, "r", newline="") as file:
                csv_reader = csv.reader(file)
                next(csv_reader)
                for row in csv_reader:
                    self.cursor.execute(f"INSERT INTO cars VALUES (NULL, ?, ?, ?, ?, ?, ?)", row)
            self.db.commit()
            print("Data imported successfully.")
        except sqlite3.Error as e:
            print(f"Error importing data: {e}")
