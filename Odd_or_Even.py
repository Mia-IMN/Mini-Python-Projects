# This app takes in a number and tells if it's an odd or even number.

# Getting input from user
number = int(input("Enter any number of your choice: "))

# Conditional statements that check the user's input
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")