# a grading system program
_score = int(input("Enter the student's score : "))
if (_score>=80):
    Grade = "A"
    print("The grade is ",Grade)
elif(_score>=60):
    Grade = "B"
    print("The grade is ",Grade)
elif(_score>=50):
    Grade = "C"
    print("The grade is ",Grade)
elif(_score>=35):
    Grade = "D"
    print("The grade is ",Grade)
elif(_score>=0):
    Grade = "F"
    print("The grade is ",Grade)
else:
    print("you entered the wrong score.")
    
