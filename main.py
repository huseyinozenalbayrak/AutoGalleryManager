import Car, my_ui


def start_the_app():
    ui = my_ui.UI(["Add Car", "Search Car", "Show All Cars", "Update Car", "Delete Car", "Delete All Sales Data", "Write DB to csv", "Write DB to xlsx", "Sell Car", "Write Sales data to csv", "Write Sales to xlsx", "Import csv file to DataBase", "Exit"])
    car_instance = Car.Car()

    while True:
        ui.show_menu()
        choice = ui.get_choice()
        if choice == 1:
            car_instance.add_car()
        elif choice == 2:
            car_instance.search_car()
        elif choice == 3:
            car_instance.print_all_cars()
        elif choice == 4:
            car_instance.update_car()
        elif choice == 5:
            car_instance.delete_car()
        elif choice == 6:
            car_instance.delete_all_sales_data()
        elif choice == 7:
            car_instance.write_db_to_csv()
        elif choice == 8:
            car_instance.write_db_to_xlsx()
        elif choice == 9:
            car_instance.sell_car()
        elif choice == 10:
            car_instance.write_sales_to_csv()
        elif choice == 11:
            car_instance.write_sales_to_xlsx()
        elif choice == 12:
            car_instance.import_csv_to_sqlite()
        elif choice == 13:
            print("Exiting from the program...")
            break


start_the_app()
