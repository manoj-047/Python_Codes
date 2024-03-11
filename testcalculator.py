
print("Calculator\nPlease choose the operations which you want to perform")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Quit Calculator")


# Function for Addition
def add(a, b):
    c = a + b
    return c


# Function for Subtraction
def sub(a, b):
    c = a - b
    return c


# Function for Multiplication
def multi(a, b):
    c = a * b
    return c


# Function for Division
def div(a, b):
    c = a / b
    return c


x = float(input("Enter the Value of A: "))
y = float(input("Enter the Value of B: "))
choice = int(input("Enter the choice which you want to perform: "))
try:
    if choice == 1:
        result = add(x, y)
        print("The result is: ", result)
    elif choice == 2:
        result = sub(x, y)
        print("The result is: ", result)
    elif choice == 3:
        result = multi(x, y)
        print("The result is: ", result)
    elif choice == 4:
        if y == 0:
            print("Cannot divide it by zero")
        else:
            result = div(x, y)
            print("The result is: ", result)
    elif choice == 5:
        exit()
    else:
        print(f"Your Choice {choice} is Invalid!. Enter a valid choice")
except ValueError:
    print(f"{choice} is not valid input.  Please enter 1, 2, 3, 4 or 5.")

