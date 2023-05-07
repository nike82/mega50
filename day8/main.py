#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#
#     match user_action:
#         case "add":
#             todo = input("Enter a todo: ") + "\n"
#             with open("./files/todos.txt", "r") as file:
#                 todos = file.readlines()
#             todos.append(todo)
#             with open("files/todos.txt", "w") as file:
#                 file.writelines(todos)
#
#         case "show" | "display":
#             with open("files/todos.txt", "r") as file:
#                 todos = file.readlines()
#             for index, item in enumerate(todos):
#                 item = item.strip("\n")
#                 print(f"{index + 1}-{item}")
#
#         case "edit":
#             number = int(input("Number of te todo to edit: "))
#             number = number - 1
#             with open("files/todos.txt", "r") as file:
#                 todos = file.readlines()
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + "\n"
#             with open("files/todos.txt", "w") as file:
#                 file.writelines(todos)
#
#         case "complete":
#             number = int(input("Numbers of todo to complete: "))
#             with open("files/todos.txt", "r") as file:
#                 todos = file.readlines()
#             index = number - 1
#             todo_to_remove = todos[index].strip("\n")
#             todos.pop(index)
#             with open("files/todos.txt", "w") as file:
#                 file.writelines(todos)
#             message = f"Todo {todo_to_remove} was removed from the list."
#             print(message)
#
#         case "exit":
#             break
#         case default:
#             print("Don't be an idiot, print correct!")
#
# print("fuck off asshole!")

#########################
# Bonus
date = input("Enter today's date: ")
mood = input("How do you rate your mood today from 1 to 10? ")
thoughts = input("Let your thoughts flow: \n")

with open(f"./journal/{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)
