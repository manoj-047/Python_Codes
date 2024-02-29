try:
    num = int(input("Enter a number: "))
    if num > 0:
        if num % 2 == 0:
            print("Even")
        else:
            print("Odd")
except:
    print("Enter Positive Integers Only")