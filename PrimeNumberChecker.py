# This code checks if a given input is a prime number or not

# Welcome message
print("Welcome to Prime number checker app")

# function definition
def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")


# Getting user input
n = int(input("What number do you want to check? "))
prime_checker(number=n)