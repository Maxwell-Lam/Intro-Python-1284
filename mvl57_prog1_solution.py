'''
Program Author: Maxwell Lam
netID:mvl57
Assignment: Wizard Currency

Description: Converts wizard currency into U.S currency. 
'''
#Ask user for the number of Knuts in pocket
print("Enter the number of Knuts you have in your pocket: ",end=' ')
#Stores Knut amount into "knuts".
knuts = int(input())
#Ask user for the number of Sickles in pocket
print("Enter the number of Sickles you have in your pocket: ",end=' ')
#Stores Sickle amount into "sickles".
sickles = int(input())
#Ask user for the number of Galleons in pocket
print("Enter the number of Galleons you have in your pocket: ",end=' ')
#Stores Galleon amount into "galleons". 
galleons = int(input())


#Mathical Conversions 
''' 
If 10 pennies = 1 Knut,
1 Sickle = 29 Knuts, and
1 Galleon = 17 Sickles.

        then

1 Knut = 10 pennies,
1 Sickle = 290 pennies, and
1 Galleon = 4930 pennies.
'''

#Calculates total pennies from Wizard currency
total_pennies = (knuts * 10) + (sickles * 290) + (galleons * 4930)
#Converts total pennies into dollar amounts
usa_cash = (total_pennies / 100)
#Shows user dollar amount attained. 
print("You have a total of ${0:.2f}".format(usa_cash))

