# This app calculates the number of paint buckets you'd need 
# when given the height and width of the work area

# importing the math module so i can use the math.ceil function
import math

# function definition
# The math.ceil function round numbers up to their next higher whole number
def paint_calc(height, width, cover):
  numb_of_cans = math.ceil((height * width)/cover)
  print(f"You'll need {numb_of_cans} cans of paint.")

# Getting user inputs
test_h = int(input("What is the height of the wall in metres? "))
test_w = int(input("What is the width of the wall in metres? "))

# I'm using a fixed coverage: 5 square metres
coverage = 5

# calling the function
paint_calc(height=test_h, width=test_w, cover=coverage)
