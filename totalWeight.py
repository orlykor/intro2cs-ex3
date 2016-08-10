############################################################
#FILE: totalWeight.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program to calculate the total weight
#output (screen)
#############################################################
import math

#define variables
total_weight= 0
max_weight= 100
ring= -1
print("Insert weights one by one:")
#while its smaller then 100 continue
while total_weight <= max_weight:
    weight = int(input())
#if its smaller then -1 print the comment then continue without affecting-
# -the total
    if (weight < -1):
        print ("Weights must be non-negative")
        continue
# when its -1 its the ring then stop and write the total
    elif (weight == -1):
        print("The total packed weight is", total_weight)
        break
    total_weight = total_weight + weight
#if its more then 100, stop and write
else:
    print("Overweight! Gandalf will not approve.") 




