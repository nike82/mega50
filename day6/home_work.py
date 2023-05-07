#
# while True:
#     user_action = (input("Type add, show, edit, complete or exit: ")).strip()
#
#     match user_action:
#         case 'add':
#             todo = input("Enter a todo: ") + "\n"
#
#             file = open('files/todos.txt', 'r')
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
#             for index, item in enumerate(todos):
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
#
# #########################
# # Bonus
# contents = ["All carrots are to be sliced longitudinally.",
#             "The carrots were reportedly sliced.",
#             "The slicing process was well presented."]
#
# filenames = ["doc.txt", "report.txt", "presentation.txt"]
#
# for content, filename in zip(contents, filenames):
#     file = open(f'./files/{filename}', 'w')
#     file.write(content)
#     file.close()
# Coding Exercise 1
# Please download the essay.txt file from the resources of this article.
# Then, create a program that reads that file and prints out its text.
# The first letter of each word in the output should be uppercase.

file = open('files/essay.txt', 'r')
content = file.read()
file.close()
print(content.title())

# Coding Exercise 2
# Write a program that reads the essay.txt file and returns
# the number of characters contained in the file.

file = open('files/essay.txt', 'r')
content = file.read()
file.close()
print(len(content))

# Coding Exercise 3
# Please download the members.txt file from the resources of this article.
# Then, create a program that, whenever executed,
# asks the user to enter a new member in the command line:
# Then, the member is added to members.txt. In this case, the text file content would be:
#
# John Smith
#
# Sen Lakmi
#
# Sono Octonot
#
# Solomon Right

# new_member = input('Enter a new member: ')
# file = open('./files/members.txt', 'r')
# members = file.readlines()
# file.close()
#
# members.append(new_member.title() + '\n')
#
# file = open('files/members.txt', 'w')
# file.writelines(members)
# file.close()

# Coding Exercise 4
# Create a program that generates multiple text files by iterating over the filenames list.
# The text Hello should be written inside each generated text file.

filenames = ['file1', 'file2', 'file3']
for filename in filenames:
    file = open(f'./files/{filename}.txt', 'w')
    file.writelines('Hello')
    file.close()

# Coding Exercise 5
# Please download the three text files a.txt, b.txt, and c.txt from the resources.
# Then, create a program that reads each text file and prints out the content of each in the command line.
# The expected output would be like the following:
# I am a.
# I am b.
# I am c.
filenames = ['a.txt', 'b.txt', 'c.txt']
for file in filenames:
    file = open(f'./files/{file}', 'r')
    content = file.read()
    print(content)
    file.close()

# Bug-Fixing Exercise 1: Take a look at the code below:
#
# file = open("data.txt", 'w')
#
# file.write("100.12")
# file.write("111.23")
#
# file.close()
# The code creates a text file which contains the following content:
#
# 100.12111.23
#
# However, the correct content should be:
#
# 100.12
#
# 111.23
#
# Please fix the code so it creates the file with the correct content.

file = open('./files/data.txt', 'w')
file.write('100.12\n')
file.write('111.23\n')
file.close()

# Bug-Fixing Exercise 2: The code below tries to write the string "100.2" to the text file.
# However, there is an error. Try to fix the error.
#
# file = open("data2.txt", 'r')
# file.write("100.12")
# file.close()

file = open('./files/data2.txt', 'w')
file.write('100.12')
file.close()
