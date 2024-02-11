# This is a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Getting user height
height = input("What is your height in meters? ")

# Getting user weight
weight = int(input("What is your weight? "))

# Converting height to a floating point number as it'd be in decimal
height_float = float(height)

# Calculating the BMI using the formular in the comments above
BMI = int(weight/(height_float ** 2))

# printing out the user's BMI
print(f"Your BMI is {BMI}")