############################################################
#FILE: ithElementValue.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program to calculate the needed arrow for an orc
#output (screen)
#############################################################
import math

# define variables
arrow_1= 1
arrow_2= 1
sum_arrow= 0
orc= int(input('Which Orc do you wish to confront?'))

#for loop- for selcted orc i want the value he holds
for i in range(orc):

    if (orc == 1):
        sum_arrow = 1

    elif (orc== 2):
        sum_arrow = 1

    elif (orc == 3):
        arrow_1 = arrow_2
        arrow_2 = 1
        sum_arrow = arrow_1 + arrow_2
#i want 1 arrow to be the 2nd one and the 2nd one
# to be the sum between the last two and so on.      
    elif (orc > 3):
        arrow_1 = arrow_2
        arrow_2 = sum_arrow
        sum_arrow = arrow_1 + arrow_2 

print("The required number of arrows is", sum_arrow)   
