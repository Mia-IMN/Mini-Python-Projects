# This is a love calculator, you input two names and it calculates their love possibility

# Welcome message
print("The Love Calculator is calculating your score...")

# Getting names for calculation
name1 = input("What is your name? ")
name2 = input("What is their name? ")

# I combined the names so I can work with just one variable and not two (name1 and name2)
combined_names = name1 + name2

# Converting to lowercase for uniformity
combined_names_lowercase = combined_names.lower()

# counting the number of occurrence of "TRUE" and "LOVE" in the given name (That's how the love calculation works)
t = combined_names_lowercase.count("t")
r = combined_names_lowercase.count("r")
u = combined_names_lowercase.count("u")
e = combined_names_lowercase.count("e")

l = combined_names_lowercase.count("l")
o = combined_names_lowercase.count("o")
v = combined_names_lowercase.count("v")
e = combined_names_lowercase.count("e")

# summing up the values
first_digit = t + r + u + e
last_digit = l + o + v + e

# Arriving at the final score
score = int(str(first_digit) + str(last_digit))

# Final print out.
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")