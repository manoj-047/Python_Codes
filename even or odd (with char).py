
# Author : Manoj G
# Date : 10-03-2024
# Batch : 3:30 - 5:30
# Description : Program to check if the given number is odd or even. This program checks
#               if the number is odd or even if the input is given in characters(one - ten)


print("Welcome to Even/Odd Checker")

while True:
    choice = input("1. Check Even/Odd(From 1 to 10) \n2. Exit\n Choose an option: ").lower()

    if choice == 2:
        exit()
    elif choice == '1':
        user_input = input("Enter a number: ").lower()  # Convert input to lowercase
        try:
            num = int(user_input)
        except ValueError:
            try:
                num = int(user_input.replace('one', '1').replace('two', '2').replace('three', '3').replace('four', '4').replace('five', '5').replace('six', '6').replace('seven', '7').replace('eight', '8').replace('nine', '9').replace('ten', '10'))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

        if num % 2 == 0:
            print(num, "is even.")
        else:
            print(num, "is odd.")
    else:
        print("Invalid choice. Please enter '1' for odd/even check or 'exit' to quit.")
