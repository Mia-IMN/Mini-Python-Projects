# This is an improved version of the previous BMI calculator
# Unlike the previous one where you'd just see your score
# This app would tell you in words if you're healthy or obese

# Welcome note
print("Welcome to the upgraded BMI calculator")

# Getting user height in meters
height = float(input("What is your height in meters: "))

# Getting user weight in kilograms
weight = int(input("What is your weight in kilograms: "))

# Calculating user BMI
BMI = round(weight/height ** 2, 2)

# Conditional statements
if BMI <= 18.5:
  print(f" Your BMI is {BMI}, you are underweight.")
elif BMI > 18.5 and BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI} you are clinically obese.")