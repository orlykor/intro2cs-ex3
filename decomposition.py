############################################################
#FILE: decomposition.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program to place the value to the day
#output (screen)
#############################################################
import math

#define variables
num_drink= int(input('Insert composed number:'))
day= 1

#while the input is bigger then 0:
while num_drink > 0:
    # calculates the modulo and saves it
    new_num = num_drink % 10
    print('The number of goblets Gimli drank on day', day,'was', new_num)
    #calculates the new number, after reducing the remain
    num_drink = int(num_drink/ 10)
    #continue to the next day
    day += 1
    
   
