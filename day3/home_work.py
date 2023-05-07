# Coding Exercise 1
# Create a program that does the following:
#
# 1. Prompts the user to input the country they are from.
#
# 2. If the user enters the word USA, the program prints out Hello.
#
# 3. If the user enters the word  India, the program prints out Namaste.
#
# 4. If the user enters the word Germany, the program prints out Hallo.
#
# Note: Strings are case-sensitive in Python, meaning germany and Germany are treated as two different strings.

# while True:
#     user_action = ((input("Input the country you are from (USA, India, Germany): ")).strip()).capitalize()
#
#     match user_action:
#         case 'USA' | 'Usa':
#             print('Hello')
#         case 'India':
#             print('Namaste')
#         case 'Germany':
#             print('Hallo')
#         case default:
#             print("Don't be an idiot, print correct!")
#             break
#
# print("Fuck off asshole!")

# Coding Exercise 2
# ingredients = ["john smith", "sen plakay", "dora ngacely"]
# Copy-paste the above line into your IDE and write a for-loop below that line
# that makes the program produce the following output:
# John Smith
# Sen Plakay
# Dora Ngasely
# Tip:  Use the str.title() method to convert strings to Title Case.

# ingredients = ["john smith", "sen plakay", "dora ngacely"]
#
# for name in ingredients:
#     print(name.title())

# Bug-Fixing Exercise 1
# The programmer is trying to loop over the buttons list and print out each item with the first letter capitalized.
# However, the programmer has done something wrong. Try to find and fix the issue.
#
# for i in buttons:
#     print(i.capitalize())
#
# buttons = ["cancel", "reply", "submit"]

buttons = ["cancel", "reply", "submit"]
for i in buttons:
    print(i.capitalize())

# Bug-Fixing Exercise 2
# The programmer is again missing something in the code. Try to find what it is and fix it.
#
# buttons = ["cancel", "reply", "submit"]
#
# for i in buttons:
# print(i.capitalize())

buttons = ["cancel", "reply", "submit"]

for i in buttons:
    print(i.capitalize())

# Bug-Fixing Exercise 3
# The code below is supposed to print out the items of the list with the first character of each item capitalized.
# However, the code contains two errors. Try to find and fix the errors.
#
# for item in ["sandals", "glasses", "trousers"):
#     print(item.capitalize)

for item in ["sandals", "glasses", "trousers"]:
    print(item.capitalize())
