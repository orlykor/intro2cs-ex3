############################################################
#FILE: findSecondSmallest.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program to find the second smallest dancer
#output (screen)
#############################################################
import math

#define variabels
dancers= 10
s_smallest= 120
secondsmallest_position= 0
smallest=120
smallest_position= 0
counter= 1

#i want the loop to run through all the dancers
while counter <= dancers:
    age = float(input("What is the age of the current dancer?"))
    #if the num is the smallest: put the age and the position of the smallest
    #to the second smallest and update the new age for the smallest one.
    if (age < smallest):
        s_smallest = smallest
        secondsmallest_position = smallest_position
        smallest = age
        smallest_position = counter
    #if not, then do that:
    elif (age < s_smallest):
        s_smallest = age
        secondsmallest_position = counter
    counter += 1
#print me the num of the position of the second smallest one.
print("Pippin is dancer number", secondsmallest_position)
         
        
         
        
    
