# A fun app that marks a treasure spot :)

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure? (A1, A2, A3, B1, B2, B3, C1, C2, or C3) ") 

# First I assigned the first character of the user's input to a variable
# I changed it to lowercase so I can have same case regardless of their input's letter case
letter = position[0].lower()

# I put the possible inputs into a list
letters = ["a", "b", "c"]

# This gets the index of the user's input from their position on the previous list I created
letter_index = letters.index(letter)

# Assigning the next character(which is a number) to a variable
# I converted it to an integer because it was previously a string (because it's an input)
# I subtracted 1 from it because counting starts from 0 around here :)
number = int(position[1]) - 1

# Writing the code that does the magic
map[number][letter_index] = "X"

# Boom!!
print(f"{line1}\n{line2}\n{line3}")