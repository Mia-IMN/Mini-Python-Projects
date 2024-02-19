# This program assigns students grade to it's interpretation

# student scores dictionary
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

# Creating a new dictionary
student_grades = {}

# Adding the grades to student_grades
for key in student_scores:
  if student_scores[key] > 90:
    student_grades[key] = "Outstanding"
  elif student_scores[key] > 80 and student_scores[key] < 91:
    student_grades[key] = "Exceeds Expectations"
  elif student_scores[key] > 70 and student_scores[key] < 81:
    student_grades[key] = "Acceptable"
  else:
    student_grades[key] = "Fail"

# Printing out the value of student_grades
print(student_grades)