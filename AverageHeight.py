# This app helps demonstrate the power of a for loop
# It determines the average height of a group of student heights input

# Getting an input of a list of student heights
# I had to split the input and make a python list out of it
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

# Declaring variables
total_height = 0
num_of_students = 0

# Using a for loop to get the total height and number of students
for height in student_heights:
  total_height += height
  num_of_students = num_of_students + 1

# Calculating the average height
average_height = total_height/num_of_students

# Printing the results
print(f"total height = {total_height}")
print(f"number of students = {num_of_students}")
print(f"average height = {round(average_height)}")