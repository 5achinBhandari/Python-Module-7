airport_data = {}
while True:

    print("\nHow would you like to proceed?")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")


    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":

        icao_code = input("Enter the ICAO code of the airport: ").upper()
        airport_name = input("Enter the name of the airport: ")


        airport_data[icao_code] = airport_name
        print(f"New airport added: {icao_code} - {airport_name}")

    elif choice == "2":

        icao_code = input("Enter the ICAO code of the airport: ").upper()


        if icao_code in airport_data:
            print(f"Airport Information: {icao_code} - {airport_data[icao_code]}")
        else:
            print("Airport not found.")

    elif choice == "3":

        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please choose a valid option (1/2/3).")


