# This app go through the range of a given number, finds even numbers and sums them up
# this is a practice on the use of range so inasmuch as there are easier ways of doing this
# I'd be using the for and range functions

# Getting user input
target = int(input("Enter a number between 0 and 1000: ")) # 

# Declaring a total sum variable
total_even_sum = 0

# Using a for loop to get and add all even numbers
for even_num in range(2, target + 1, 2):
  total_even_sum += even_num

# printing final result
print(total_even_sum)
  