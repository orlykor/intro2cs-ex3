############################################################
#FILE: findLargest.py
#WRITER: orlykoren, orlykor12, 203595541
#EXERCISE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program to find the max number
#output (screen)
#############################################################
import math


#enter the variabels i need for the program
num_riders= int(input("Enter the number of riders:")) 
counter= 0
max_position= 1
max_hat= 0

#do a while loop, go through all the riders, then stop
while counter < num_riders:

    new_hat = float(input("How tall is the hat?"))
    counter += 1 #put hight for the hat, then go to the next rider
    if (new_hat > max_hat): #if the given hat is bigger then the max:
        max_position = counter #change the max pos. to the counter
        max_hat = new_hat #now the max hat is the new one
print("Gandalf's position is:",max_position)
    

    
 
