# Author : Manoj G
# Date : 16-02-2024
# Batch : 3:30 - 5:30
# Description : Print multiplication tables using for loop in reverse


s = int(input('Enter Starting Table: '))
e = int(input('Enter Ending Table: '))
for j in range(e, s, ):
    for i in range(1, 11):
        print(j, '*', i, '=', s*i)
