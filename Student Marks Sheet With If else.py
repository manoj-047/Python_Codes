# Author : Manoj G
# Date : 13-02-2024
# Batch : 3:30 - 5:30
# Description : Student Marks sheet using if else stmt


print('Student Marks Sheet\n')
name = input('Enter Student Name: ')
print('Enter Subject Marks')
sub1 = int(input('English: '))
sub2 = int(input('Kannada: '))
sub3 = int(input('Maths: '))
sub4 = int(input('Science: '))
sub5 = int(input('Social: '))
sub6 = int(input('Sanskrit: '))
if (sub1<0) or (sub1>100) or (sub2<0) or (sub2>100) or (sub3<0) or (sub3>100) or (sub4<0) or (sub4>100) or (sub5<0) or (sub5>100) or (sub6<0) or (sub6>100):
    print('Entered Incorrect Marks')
    exit()
else:
    pass
print('English : ', sub1)
print('Kannada : ', sub2)
print('Maths   : ', sub3)
print('Science : ', sub4)
print('Social  : ', sub5)
print('Sanskrit: ', sub6)
total = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
print('Total Marks = ', total)
percentage = (6/total)*100
if total > 500:
    print('Sumanth got ', percentage, '% with Distinction')
elif total > 423 and total < 549:
    print('Sumanth got ', percentage, '% with First Class')
elif total > 330 and total < 422:
    print('Sumanth got ', percentage, '% with Second Class')
elif total < 330:
    print('Sumanth Failed')
else:
    pass
