# Write a program that asks users to enter a password.
# Then, it checks if the password length is greater than 7 and returns "Great password there!".
# If the password has 7 or fewer characters, the program returns, "Your password is weak".
# Extend the program we built in Coding Exercise 1 by adding a new feature.
# The new feature should allow the program to return "Password is OK, but not too strong"
# when the password is exactly seven characters long.

# password = input("Enter new password: ")
#
# if len(password) > 7:
#     print("Great password there!")
# elif len(password) < 7:
#     print("Your password is weak!")
# else:
#     print("Password is OK, but not too strong!")

# Bug-Fixing Exercise 1: The program below intends to find out how many items have
# at least one underscore ("_") character in them.
# However, there is an error with the code. Try to find and fix it.
#
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
# if '_' in id:
#     x = x + 1
# print(x)

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x += 1
print(x)

# Bug-Fixing Exercise 2: This program also intends to find out how many items have an underscore in them.
# However, the program has a bug. It doesn't return an error message, but it returns:
#
# 1
# 1
# 2
# Instead, the expected output is:
#
# 2
#
# Try to fix the program, so it returns the expected output. Here is the buggy program:
#
# ids = ["XF345_89", "XER76849", "XA454_55"]
#
# x = 0
#
# for id in ids:
#     if '_' in id:
#         x = x + 1
#     print(x)

ids = ["XF345_89", "XER76849", "XA454_55"]

x = 0

for id in ids:
    if '_' in id:
        x += 1
print(x)

# Bug-Fixing Exercise 3: Fix the program below, so it prints out "OK"
# when the perimeter is less than 14 and the area is less than 8.
#
# length = float(input("Enter length: "))
# width = float(input("Enter width: "))
#
# perimeter = (length + width) * 2
# area = length * width
#
# print("Perimeter is", perimeter)
# print("Area is", area)
#
# if perimeter < 14 and area > 10:
#     print("OK")
# else:
#     print("NOT OK")

length = float(input("Enter length: "))
width = float(input("Enter width: "))

perimeter = (length + width) * 2
area = length * width

print("Perimeter is", perimeter)
print("Area is", area)

if perimeter < 14 and area < 8:
    print("OK")
else:
    print("NOT OK")
