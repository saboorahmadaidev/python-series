# Control Statements
# Check if number is positive, negative, or zero

n = int(input("Enter a Number:"))
if n > 0 :
    print("The Number Is Positve")
elif n < 0:
    print("The Number Is Negative")
else :
    print("Zero")
    
# Simple grading system
marks = int(input("Enter marks (0-100): "))
if marks > 80 :
   grade = "A+"
elif marks > 70 : 
   grade = "A"
elif marks > 60 :
    grade = "B"
elif marks >= 50:
    grade = 'C'
else:
    grade = 'F'
    
print(f"Marks = {marks} -> Grade: {grade}")
