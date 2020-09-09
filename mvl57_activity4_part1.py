'''
Program Author: Maxwell Lam
netID:mvl57
Assignment: Acitivty 4 Part 1

'''
#Ask for user's letter grade.
letter_grade = input("REPORT YOUR LETTER GRADE IMMEDIATELY!!!   ")

#Converts letter grade into gpa value. 
if letter_grade == "A":
    gpa = 4.0
elif letter_grade == "B":
    gpa = 3.0
elif letter_grade == "C":
    gpa = 2.0
elif letter_grade == "D":
    gpa = 1.0
elif letter_grade == "F":
    gpa = 0.0
else:
    gpa = -1.0

#Print out gpa value to user on screen. 
print("Your GPA is",gpa)
