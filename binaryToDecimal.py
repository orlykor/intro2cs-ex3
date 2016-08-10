############################################################
#FILE: binaryToDecimal.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex3 2014-2015
#DESCRIPTION:
#convert binary numbers into decimal
#output (screen)
#############################################################
import math
#define variables
num= int(input('Insert number in binary representation:'))   
base_2= 2**0
sum_decimal= int()


while num > 0:

    last_digit = num % 10 #i want the last digit
    binary = base_2 * last_digit #turn it to decmial digit
    num = int(num / 10)
    base_2 = (base_2) * 2 # while we go with the numbers the base 2 is doubled
    sum_decimal += binary

print('The decimal value of the inserted binary number is', sum_decimal)

