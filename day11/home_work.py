# Coding Exercise 1
# The code below is incomplete. It should calculate and print out
# the maximum value of the grades list. Please complete the function and then call it.
#
# def get_max():
#     grades = [9.6, 9.2, 9.7]
# The output of your code should be:
#
# 9.7
#
# Hint: You can use the max(list) function to find the maximal value of a list.


def get_max():
    grades = [9.6, 9.2, 9.7]
    return max(grades)


print(get_max())

# Coding Exercise 2
# The function we wrote in exercise 1 returned 9.7.
# Change the function so this time it returns Max: 9.7, Min: 9.2 where 9.7 is the maximum and 9.2 is the minimum.


def get_max_min():
    grades = [9.6, 9.2, 9.7]
    return f"Max: {max(grades)}, Min: {min(grades)}"


print(get_max_min())

# Bug-Fixing Exercise 1
# The following get_maximum function is designed to return the maximum value of the celsius list,
# while the last two lines of the code will convert the celsius value to Fahrenheit and print it out.
#
# def get_maximum():
#     celsius = [14, 15.1, 12.3]
#     maximum = max(celsius)
#     print(maximum)
#
# celsius = get_maximum()
#
# fahrenheit = celsius * 1.8 + 32
# print(fahrenheit)
# However, when running the code, the following error is generated:
#
# TypeError: unsupported operand type(s) for *: 'NoneType' and 'float'
#
# Try to fix the problem so that the last two lines can correctly get the maximal celsius
# value from the function definition and convert that value to Fahrenheit.


def get_maximum():
    celsius_local = [14, 15.1, 12.3]
    maximum = max(celsius_local)
    return maximum


celsius = get_maximum()

fahrenheit = celsius * 1.8 + 32
print(fahrenheit)
