# This app picks a name out of a list of names
import random

# Getting input from user
names_string = input("Enter the list of names. Each name should be followed by a comma and space: ")

# splitting and storing input into a list
names = names_string.split(", ")

# Getting the number of name input the user provided
length = len(names)

# Rolling the dice
dice = random.randint(0, length - 1)

# Final output
print(f"{names[dice]} is going to buy the meal today!")