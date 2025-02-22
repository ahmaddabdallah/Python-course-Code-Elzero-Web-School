# Taking user input for the student's score
score = int(input("Enter the Student's score: "))

# Using if, elif, and else to classify the grade
if score >= 90:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
else:
    grade = 'F'

# Displaying the result
print(f"The student's grade is: {grade}")