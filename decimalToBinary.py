############################################################
#FILE: decimalToBinary.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex3 2014-2015
#DESCRIPTION:
#convert decimal numbers into binary
#output (screen)
#############################################################
import math

#define variables
num_decimal= int(input("Insert number in decimal representation:"))
sum_binary= str() #the string of the binary numbers

while num_decimal > 0:
    binary_digit = str(num_decimal % 2) #the binary digit 1 or 0
    num_decimal = num_decimal // 2 # the number i put divine by 2
    sum_binary = binary_digit + sum_binary 
    
    
print("The binary value of the inserted decimal number is", sum_binary)
    


