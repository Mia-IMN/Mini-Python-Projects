# This app gets the highest number of a range of numbers
# This is another practice on using the for loop 
# So inasmuch as there are several other easy ways to do this, 
# I'd be using just the for loop

# Getting input
student_scores = input("Input a list of student scores: ").split()

# Storing the input into list
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# declaring the highest score variable
highest_score = 0

# Using a for loop to get the highest score
for score in student_scores:
  if score > highest_score:
    highest_score = score
  
# Final output
print(f"The highest score in the class is: {highest_score}")