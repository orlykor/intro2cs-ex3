############################################################
#FILE: twoDimentionalSeek.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program to help Gandalf find sam and frodo
#output (screen)
#############################################################
import math

#define variables
sum_x= 0
sum_y= 0

turn= str(input('Next turn:'))
direction= 'forward'
direction_x= ''
direction_y= ''

#while the turn is not the end:
while turn != 'end':
    step= int(input('How many steps?'))
    #the begining point is when we turn forward
    if (direction == 'forward'):   
    #if we tun right, its right-if left its left
        if (turn == 'right'):
            direction = 'right'
            sum_x= sum_x + step #add plus the steps we entered to the sum
        elif (turn == 'left'):
            direction = 'left'
            sum_x= sum_x - step #the left steps is minus to the sum
    elif (direction == 'backward'): #now, if we are looking backward its:
        if (turn == 'right'): #right is left
            direction = 'left'
            sum_x= sum_x - step #so we need to do minus to the sum
        elif (turn == 'left'):
            direction = 'right' #left= right, and we need to add
            sum_x= sum_x + step
    elif (direction == 'right'): #now if we are looking east-or right its:
        if (turn == 'right'):   #right is bacward and its minus to the sum
            direction = 'backward'
            sum_y= sum_y - step
        elif (turn == 'left'): 
            direction = 'forward' #left is forward and its plus to the sum
            sum_y= sum_y + step
     #now if we are looking west-or left its the opposite from before.
    elif (direction == 'left'): 
        if (turn == 'right'):
            direction = 'forward'
            sum_y= sum_y + step
        elif (turn == 'left'):
            direction = 'backward'
            sum_y= sum_y - step
    turn= str(input('Next turn:'))
    #i want all the sums to be plus:
if (sum_x < 0): #if its minus, then its left.
    sum_x = abs(sum_x) 
    direction_x= 'left' 
elif (sum_x >= 0):
    direction_x= 'right'
    sum_x = sum_x
if (sum_y < 0): #if here its minus then its backward
    direction_y= 'backward'
    sum_y= abs(sum_y)
elif (sum_y >= 0):
    direction_y = 'forward' 
    sum_y= sum_y

print("Gandalf should fly", sum_x, "steps", direction_x, "and", sum_y, 
"steps", direction_y)
 




