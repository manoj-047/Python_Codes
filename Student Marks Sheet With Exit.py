# Author : Manoj G
# Date : 15-02-2024
# Batch : 3:30 - 5:30
# Description : Create student mark sheet with if condition.
#               Whn giving the input marks if any marks is less than 0 and greater than 100 thn it will exit


print('Student Marks Sheet')
name = input('Enter Student Name: ')
print('Enter Subject Marks')
sub1 = int(input('English: '))
if sub1 < 0 or sub1 > 100:
    exit()
else:
    print(sub1)
sub2 = int(input('Kannada: '))
if sub2 < 0 or sub2 > 100:
    exit()
else:
    print(sub2)
sub3 = int(input('Maths: '))
if sub3 < 0 or sub3 > 100:
    exit()
else:
    print(sub3)
sub4 = int(input('Science: '))
if sub4 < 0 or sub4 > 100:
    exit()
else:
    print(sub4)
sub5 = int(input('Social: '))
if sub5 < 0 or sub5 > 100:
    exit()
else:
    print(sub5)
sub6 = int(input('Sanskrit: '))
if sub6 < 0 or sub6 > 100:
    exit()
else:
    print(sub6)
total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
print('Total Marks = ', total)
percentage = (total/600)*100
if total >= 500:
    print('Sumanth got ', percentage, '% with Distinction')
elif total >= 450 and total < 500:
    print('Sumanth got ', percentage, '% with First Class')
elif total >= 330 and total < 450:
    print('Sumanth got ', percentage, '% with Second Class')
else:
    print('Sumanth Failed')
