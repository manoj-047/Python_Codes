# Author : Manoj G
# Date : 28-02-2024
# Batch : 3:30 - 5:30
# Description : read a binary file using file method and print the output  in a
#               seperate txt file


file = open("screenshot.png", "rb")
val = file.read()
file.close()
file = open("screenshot.txt", "wb")
file.write(val)
file.close()
