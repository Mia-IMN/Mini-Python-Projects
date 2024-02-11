# This bunch of code is meant to tell a user the amount of weeks he/she has left, assuming they make it up to 90yrs
# This serves as a reminder of how precious life is and how little moments matter a lot.

#Introduction message
print("Hi, Welcome to Life In Weeks App")
print("We all know how precious life is but sometimes a quick reminder help us remember how precious little moments can be")

# Getting user age input
age = input("How old are you? ")

# Calculating number of weeks left
weeks_left = (90 - int(age)) * 52

# Final result
print(f"You have {weeks_left} weeks left.")
print("Make the best out of them.")