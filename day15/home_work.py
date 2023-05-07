# Coding Exercise 1
# Your task is to create a program that generates a random whole number.
# Here is how the program should behave:

# Enter the lower bound: 7
#  Enter the upper bound: 10
# 9

# Note: To create this program, you might need to do some internet research or use the Python module index
# to find out what module and what function of that module you can use to generate random numbers.
# While it is easy for me to provide some clues here on what module you should use, searching for information
# and becoming familiar with programming community sites such as
# Stackoverflow is part of the programming skill-set you should acquire.
# Thus, it is essential to practice such skills as well, so you are independent after you finish the course.

from random import randrange

lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

print(randrange(lower_bound, upper_bound + 1))
