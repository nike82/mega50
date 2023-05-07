# Create a function that converts liters to cubic meters knowing that 1000 liters make 1 cubic meter.
def liter_to_cube_meter(liter):
    return liter / 1000


print(liter_to_cube_meter(2))


# Coding Exercise 2
# Create a script that asks the user to enter a password.
# Then create a function that checks the strength of the user password.
# The function should return Strong Password if all of the following conditions are true:
#
# Eight or more characters
#
# At least one uppercase letter.
#
# At least one digit.

def check_password(password):
    length = False
    upper = False
    digit = False
    if len(password) >= 8:
        length = True

    for char in password:
        if char.isupper():
            upper = True
            break
    for char in password:
        if char.isdigit():
            digit = True
            break
    if length and upper and digit:
        return "Password is strong!"
    return "Password is weak!"



password = input("Enter the password: ")

print(check_password(password))

feet_inches = input("Enter feet and inches: ")

def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches + 0.0254
    return meters

result = convert(feet_inches)

if result < 1:
    print("Kid is too small!")
else:
    print("Kid can use the slide!")


# Bug-Fixing Exercise 1
# Alina has created a speed calculation function. She traveled a total of 200 miles today which took her two hours.
# She wants to use her function to calculate the average speed.
#
# def speed(distance, time):
#     return distance / time
#
# print(speed([200, 4]))
# However, when she calls the function (as you see below), she gets an error:
#
# TypeError: speed() missing 1 required positional argument: 'time'
#
# Try fixing the code so she gets 50 as output.

def speed(distance, time):
    return distance / time

print(speed(200, 4))

# Bug-Fixing Exercise 2
# This time, Alina traveled 300 miles and it took her 5 hours.
# However, she is not getting the correct output from its function. Try fixing the code:
#
# def speed(distance, time):
#     return distance / time
#
# print(speed(5, 300))

def speed(distance, time):
    return distance / time

print(speed(300, 5))