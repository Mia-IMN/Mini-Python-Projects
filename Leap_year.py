# This app takes in a year as input and tells if it's a leap year or not

# Welcome message
print("Get to know which year is a leap year and which isn't")

# Getting user's input
year = int(input("Enter year: "))

# Conditional statements
if year % 4 == 0:
  if year % 100 == 0:
    print("Not leap year")
  elif year % 400 == 0:
    print("Leap year")
  else: 
    print("Leap year")
else:
  print("Not leap year")