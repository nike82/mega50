# task 1
# Create a program that prompts the user to input their name once.
# Then, the program prints out the name once with the first letter capitalized.

user_prompt = input("Enter your name: ")
print(user_prompt.capitalize())

# task 2
# Create a program that prompts the user to input their name once.
# Then, the program repeatedly prints out the name with the first letter capitalized.

user_prompt = input("Enter your name: ")
while True:
    print(user_prompt.capitalize())

# task 3
# Create a program that prompts the user to input their name repeatedly.
# Then, the program repeatedly prints out the name with the first letter capitalized.

while True:
    user_prompt = input("Enter your name: ")
    print(user_prompt.capitalize())


# Bugfix
# Bug-Fixing Exercise 1
# The code below has two bugs. Hunt them down and fix them.
# while True
# print("Hello")

while True:
    print("Hello")

# Bug-Fixing Exercise 2
# The programmer here is trying to convert the string "hello" to "HELLO" by using the upper() method:
#
# greeting = "hello"
# print(upper(greeting))

greeting = "hello"
print(greeting.upper())

# Bug-Fixing Exercise 3
# A programmer wrote the following program:
#
# countries = []
#
# while True:
#     country = input("Enter the country: ")
#     countries.append(country)
# print(countries)

countries = []

while True:
    country = input("Enter the country: ")
    countries.append(country)
    print(countries)

