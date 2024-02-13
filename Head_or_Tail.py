# This app acts as a die, randomly choosing between heads or tails

# Importing the random module
import random

# Using the random module to choose either a 0 or 1
random_num = random.randint(0,1)

if random_num == 0:
  print("Tails")
else:
  print("Heads")