# Author : Manoj G
# Date : 13-03-2024
# Batch : 3:30 - 5:30
# Description : Conversion of a given number to binary, octal, hexadecimal

num = int(input("Enter a number: "))
i = 0
while i <= num:
    i += 1
    print("\nNum: ", num)
    print("Binary: ", bin(i))
    print("Octa: ", oct(i))
    print("Hexadecimal: ", hex(i))
