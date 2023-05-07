#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#
#     if "add" in user_action:
#         todo = user_action[4:]
#         with open("./files/todos.txt", "r") as file:
#             todos = file.readlines()
#         todos.append(todo)
#         with open("files/todos.txt", "w") as file:
#             file.writelines(todos)
#
#     elif "show" in user_action:
#         with open("files/todos.txt", "r") as file:
#             todos = file.readlines()
#         for index, item in enumerate(todos):
#             item = item.strip("\n")
#             print(f"{index + 1}-{item}")
#
#     elif "edit" in user_action:
#         number = int(user_action[5:])
#         number = number - 1
#         with open("files/todos.txt", "r") as file:
#             todos = file.readlines()
#         new_todo = input("Enter new todo: ")
#         todos[number] = new_todo + "\n"
#         with open("files/todos.txt", "w") as file:
#             file.writelines(todos)
#
#     elif "complete" in user_action:
#         number = int(user_action[9:])
#         with open("files/todos.txt", "r") as file:
#             todos = file.readlines()
#         index = number - 1
#         todo_to_remove = todos[index].strip("\n")
#         todos.pop(index)
#         with open("files/todos.txt", "w") as file:
#             file.writelines(todos)
#         message = f"Todo {todo_to_remove} was removed from the list."
#         print(message)
#
#     elif "exit" in user_action:
#         break
#     else:
#         print("Don't be an idiot, print correct!")
# print("fuck off asshole!")

#########################
# Bonus
password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False

digit = False
for char in password:
    if char.isdigit():
        digit = True
        break

result["digits"] = digit

is_upper = False
for char in password:
    if char.isupper():
        is_upper = True
        break

result["upper-case"] = is_upper
print(result)

if all(result.values()):
    print("Strong password!")
else:
    print("Weak password!")
