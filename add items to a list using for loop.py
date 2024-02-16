# Author : Manoj G
# Date : 16-02-2024
# Batch : 3:30 - 5:30
# Description : append a set number of elements into a list using for loop


list1 = []
n = int(input('Enter the number of elmts to add: '))
for i in range(0, n):
    inp = input('Enter the elements: ')
    list1.append(inp)
print(list1)