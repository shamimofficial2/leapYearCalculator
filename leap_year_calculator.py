def leap_year(year):

    try:
        year = int(year)

    except ValueError:
         return "Invalid input. Please enter a integer value."
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"\033[32m{year}\033[0m\033[37m is Leap Year\n"
    
    else:
        return f"\033[31m{year}\033[0m\033[37m is not Leap Year\n"
    
while True:
    user_input = input("Enter a year ('quit' to exit): ").strip()
    if user_input.lower() == "quit":
        break

    else:
        try:
            user_input = int(user_input)
        except ValueError:
            print("\033[33mInvalid input. Please enter an integer value.\033[0m\033[37m")
            print("\n")
            continue

    print(leap_year(user_input))