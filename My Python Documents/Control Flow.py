''' Student Grading Script
by Erim Serdönmez '''

# Ask student for their mark

mark = int(input ("Please Enter Test Mark (0 - 100)... "))

# Award correct grade

'''
A: 90 - 100
B: 70 - 89
C: 50 - 69
D: 30 - 49
F: 0 - 29
'''

if mark >= 90:
    grade = "A"
# Remember the strings and int relations
elif mark >= 70:
    grade = "B"

elif mark >= 50:
    grade = "C"

elif mark >= 30:
    grade = "D"

else:
    grade = "F"

    
# Print grade to UI/console

if grade == "F":
    print (" Sorry, you've failed" + grade)
else :
    print ("You done good." + grade )
