
# Coding Exercise 1
# Create a program that:
#
# 1. Prompts the user to input a (dollar) amount.
#
# 2. Calculates the corresponding amount in euros, given an exchange rate of 0.95.
#
# 3. Prints out the amount in euros, as shown in the screenshot below.

amount_usd = float(input("How many bucks you got? "))
print(f'The amount in euros is: {amount_usd * 0.95}')

################################################
# Coding Exercise 2
# The list below represents the ranking of three athletes. John won 1st place, Sen got 2nd, and Lisa the 3rd.
#
# ranking = ['John', 'Sen', 'Lisa']
#
#
#
# Create a program that:
#
# 1. Contains the above list.
#
# 2. Prompts the user to input a rank number.
#
# 3. Returns the person who has the given rank.

ranking = ['John', 'Sen', 'Lisa']

while True:
    user_action = int(input("Input rank number (1, 2, 3): ")) - 1

    match user_action:
        case 0:
            print(ranking[0])
            break
        case 1:
            print(ranking[1])
            break
        case 2:
            print(ranking[2])
            break
        case default:
            print("Don't be an idiot, print correct!")

###
ranking = ['John', 'Sen', 'Lisa']
user_action = int(input("Input rank number (1, 2, 3): ")) - 1
print(ranking[user_action])

#################################
# Coding Exercise 3
# We have the same list:
#
# ranking = ['John', 'Sen', 'Lisa']
#
# This time you need to create a program that:
#
# 1. Contains the above list.
#
# 2 Prompts the user to input the person's name.
#
# 3. Returns the rank that person has.

ranking = ['John', 'Sen', 'Lisa']

while True:
    user_name = (input("Input person name to get its rank: "))

    match user_name:
        case 'John':
            print(int(ranking.index('John')) + 1)
            break
        case 'Sen':
            print(int(ranking.index('Sen')) + 1)
            break
        case 'Lisa':
            print(int(ranking.index('Lisa')) + 1)
            break
        case default:
            print("Don't be an idiot, print correct!")

###

ranking = ['John', 'Sen', 'Lisa']
user_name = input("Input person name to get its rank: ")
print(int(ranking.index(user_name)) + 1)

####################################################
# Bug-Fixing Exercise 1
# The programmer is trying to extract and print out 'b' using list indexing, but there is an error. Try to fix it.
#
# elements = ['a', 'b', 'c']
# print(elements(1))

elements = ['a', 'b', 'c']
print(elements[1])

###################################################
# Bug-Fixing Exercise 2
# The code below aims to replace 'b' with 'x' in the list elements.
#
# However, the output of the code is still ['a', 'b', 'c'].
#
# Try to fix the code so 'b' is replaced with 'x'.
#
# elements = ['a', 'b', 'c']
# new = 'x'
# new = elements[1]
# print(elements)

elements = ['a', 'b', 'c']
new = 'x'
elements[1] = new
print(elements)
