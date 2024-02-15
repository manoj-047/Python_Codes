# Author: Manoj G
# Date: 14-02-2024
# Batch: 3:30 - 5:30
# Description: Finding whether the given input is of type string, float, int(positive or negative)


x = input("Enter a value: ")
if x.isdigit():
    print('Integer')
elif '-' in x:
    print(" Negative Number")
elif '.' in x:
    print(" Float")
else:
    print("String")
