#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ") + "\n"
#
#             file = open('./files/todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#
#             todos.append(todo)
#
#             file = open('files/todos.txt', 'w')
#             file.writelines(todos)
#             file.close()
#         case 'show' | 'display':
#             file = open('files/todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#
#            # new_todos = [item.strip('\n') for item in todos]
#
#             for index, item in enumerate(todos):
#                 item = item.strip('\n')
#                 print(f'{index + 1}-{item}')
#         case 'edit':
#             file = open('files/todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#             number = int(input("Number of te todo to edit: "))
#             number -= number
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo
#         case 'complete':
#             file = open('files/todos.txt', 'r')
#             todos = file.readlines()
#             file.close()
#             number = int(input("Numbers of todo to complete: "))
#             todos.pop(number - 1)
#         case 'exit':
#             break
#         case default:
#             print("Don't be an idiot, print correct!")
#
# print("fuck off asshole!")

#########################
# Bonus
filenames = ["1.doc", "1.report", "1.presentation"]
filenames = [filename.replace('.', '-') + '.txt' for filename in filenames]
print(filenames)

# Coding Exercise 1
# names = ["john smith", "jay santi", "eva kuki"]
#
# Extend the code above so the code capitalizes all the names and the surnames of
# the list and then prints the new list.
#
# The output of your code should be as below:
#
# ['John Smith', 'Jay Santi', 'Eva Kuki']

names = ["john smith", "jay santi", "eva kuki"]
names = [name.title() for name in names]
print(names)

# Coding Exercise 2
# usernames = ["john 1990", "alberta1970", "magnola2000"]
#
# Extend the code above so the code prints out a list containing the number of characters for each username.
#
# The output of your code should be as below:
#
# [9, 11, 11]

usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames_length_list = [len(name) for name in usernames]
print(usernames_length_list)

# Coding Exercise 3
# user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out a list containing the same items as floats.
#
# The output of your code should be as below:
#
# [10.0, 19.1, 20.0]

user_entries = ['10', '19.1', '20']
floats_list = [float(item) for item in user_entries]
print(floats_list)

# Coding Exercise 4
# user_entries = ['10', '19.1', '20']
# Extend the code above so the code prints out the sum of the numbers.
#
# The output of your code should be as below:
# Hint: Use the sum() function.
# The function gets a list of numbers as input and produces the sum of all numbers.
#
# 49.1

user_entries = ['10', '19.1', '20']
float_list = [float(item) for item in user_entries]
print(sum(float_list))

# Bug-Fixing Exercise 1
# The code below tries to write the items of temperatures each in one line in the file.txt list.
# However, the code has an error. Try to fix the error.
#
# temperatures = [10, 12, 14]
#
# file = open("file.txt", 'w')
#
# file.writelines(temperatures)

temperatures = [10, 12, 14]
file = open('./files/file.txt', 'w')
temperatures = [str(temp) + '\n' for temp in temperatures]
file.writelines(temperatures)
file.close()

# Bug-Fixing Exercise 2
# The code below tries to convert all the numbers to integers.
# However, the code has an error. Try to fix the error.
#
# numbers = [10.1, 12.3, 14.7]
# numbers = [int(number) for item in numbers]
# print(numbers)

numbers = [10.1, 12.3, 14.7]
numbers = [int(number) for number in numbers]
print(numbers)
