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
