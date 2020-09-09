'''
NetID: mvl57
Name: Maxwell Lam
Assignment: CSE 1284 fALL 2020 Activity 3 Part 1
'''

#Ask for user's height
print("What is your current height? ", end=' ')
#Stores user's height
height = input()
#Ask for user's favorite color
print("What is your favorite color? ", end=' ')
#Stores user's favorite color
color = input()

#Final Output
print("My name is mvl57! My height is ",height, "and my favorite color is ", color,".")

#Assigns the sum of 9999 and 4563 to the variable "total".
total = 9999 + 4563
#Assigns the value of 3500 to the variable "down_payment".
down_payment = 3500
#Subracts the value of "down_payment" from the value of "total" and assigns the difference into the variable "due".
due = total - down_payment

#Prints finanical output.
print("You must pay" ,due,".")
