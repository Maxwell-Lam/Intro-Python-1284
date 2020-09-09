'''
Program Author: Maxwell Lam
netID:mvl57
Assignment: Acitivty 4 Part 2

'''
x = ??

# X = { 11, 12, 13, 14 ,15, 16, 17, 18, 19 }
# for this statement to be true. 
if x > 10 and x < 20:
    print("if Statement 1 Executed!")
# No values of X would make this statment true. 
if x < 10 and x > 20:
    print("if Statement 2 Executed!")
# All numerical values would make this statement true. 
if x > 10 or x < 20:
    print("if Statement 3 Executed!")
# All values 9 and under with the value of 19
# and over would make this statement true
if x < 10 or x > 20:
    print("if Statement 4 Executed!")
# X must be 2 or 3 to make this statement true
if x == 2 or x == 3:
    print("if Statement 5 Executed!")
# All values expect for 2 and 3 would made this statement true. 
if x != 2 and x != 3:
    print("if Statement 6 Executed!")
# All values would make this statement true. 
if x != 2 or x != 3:
    print("if Statement 7 Executed!")
