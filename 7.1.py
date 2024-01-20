
seasons = ("Winter", "Spring", "Summer", "Autumn")

month_number = int(input("Enter a month number (1-12): "))


if 1 <= month_number <= 12:

    season_index = (month_number - 1) // 3
    season = seasons[season_index]

   
    print(f"The season for month {month_number} is {season}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
