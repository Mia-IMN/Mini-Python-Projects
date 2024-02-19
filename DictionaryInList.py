# A program that demonstrates the use of dictionaries in list
# It'll take in some inputs, add them to a dictionary and then to a list and then print it out

# Getting user input
country = input("Add country name: ") 
visits = int(input("Number of visits? "))
# create list from formatted string
list_of_cities = eval(input("List of city visited: "))

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# A function that will allow new countries
# to be added to the travel_log. 

def add_new_country(country, visits, list_of_cities):
  new_dictionary = {"country": country, "visits": visits, "cities": list_of_cities}
  travel_log.append(new_dictionary)


# Printing out the result
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")