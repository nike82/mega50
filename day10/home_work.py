#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith("add"):
#         todo = user_action[4:]
#         with open("./files/todos.txt", "r") as file:
#             todos = file.readlines()
#         todos.append(todo + "\n")
#         with open("files/todos.txt", "w") as file:
#             file.writelines(todos)
#
#     elif user_action.startswith("show"):
#         with open("files/todos.txt", "r") as file:
#             todos = file.readlines()
#         for index, item in enumerate(todos):
#             item = item.strip("\n")
#             print(f"{index + 1}-{item}")
#
#     elif user_action.startswith("edit"):
#         try:
#             number = int(user_action[5:])
#             number = number - 1
#             with open("files/todos.txt", "r") as file:
#                 todos = file.readlines()
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + "\n"
#             with open("files/todos.txt", "w") as file:
#                 file.writelines(todos)
#         except ValueError:
#             print("Your command is not valid!")
#             continue
#
#     elif user_action.startswith("complete"):
#         try:
#             number = int(user_action[9:])
#             with open("files/todos.txt", "r") as file:
#                 todos = file.readlines()
#             index = number - 1
#             todo_to_remove = todos[index].strip("\n")
#             todos.pop(index)
#             with open("files/todos.txt", "w") as file:
#                 file.writelines(todos)
#             message = f"Todo {todo_to_remove} was removed from the list."
#             print(message)
#         except IndexError:
#             print("No item with that number!")
#             continue
#     elif user_action.startswith("exit"):
#         break
#     else:
#         print("Don't be an idiot, print correct!")
# print("fuck off asshole!")

#########################
# Bonus
# try:
#     length = float(input("Enter length: "))
#     width = float(input("Enter width: "))
#
#     if width == length:
#         exit("That is square!")
#
#     perimeter = (length + width) * 2
#     area = length * width
#
#     print("Perimeter is", perimeter)
#     print("Area is", area)
# except ValueError:
#     print("Enter a number!")


# Coding Exercise 1
# Build a percentage calculator that gets from the user the "total value"
# and the "value" and returns the percentage as shown below:

try:
    total_value = int(input("Enter total value: "))
    value = int(input("Enter value: "))

    percent = value / total_value * 100
    print(f"That is: {percent}%")

except ValueError:
    print("Enter a number! And run the program again")

# Coding Exercise 2
# As you might know, it is not mathematically possible to divide a number by zero. Consequently,
# this is also not possible in Python either -you will get a ZeroDivisionError if you try:
#
# >>> 20 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
# With that in mind, your task for this exercise is to extend the program you created in Exercise 1
# by displaying a message to the user when they enter 0 for the "total value".

try:
    total_value = float(input("Enter total value: "))
    value = float(input("Enter value: "))

    percent = value / total_value * 100
    print(f"That is: {percent}%")

except ValueError:
    print("Enter a number! And run the program again")
except ZeroDivisionError:
    print("Zero division asshole!")

# Bug-Fixing Exercise 1
# Have a look at the program below:
#
# waiting_list = ["john", "marry"]
# name = input("Enter name: ")
#
# number = waiting_list.index(name)
# print(f"{name}'s turn is {number}")
#
#
# When the user enters the name of one of the waiting_list members,
# the program returns the index of that name. For example, when the user enters "john", 0 is printed out.
# If the user enters a name that is not in the list, such as "zen", the program throws an error.
# Change the program, so it prints out "zen is not in the list" instead of returning an error
# when the user enters "zen" or any other name that is not in the list.

waiting_list = ["john", "marry"]
name = input("Enter name: ")
if name not in waiting_list:
    exit(f"{name} is not in the list!")
number = waiting_list.index(name)
print(f"{name}'s turn is {number}")
