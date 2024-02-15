# Author : Manoj G
# Date : 13-02-2024
# Batch : 3:30 - 5:30
# Description :If the given input is in digits(Eg: '1') the output will be in words('One')


x = input('Enter a Value: ')
if x.isdigit():
        y = int(x)
        if (y % 2) == 0:
            print('Given Value Is Even Number')
        else:
            print('Given Value Is a Negative Number')
elif '-' in x:
    print('Input Is A Negative Integer, Enter Positive Value')
elif x.isalpha():
    print('Input Is A String, Enter an Integer')
elif '.' in x:
    print('Input Is A Float Value, Enter Integer Value')
else:
    print('Invalid Value')
