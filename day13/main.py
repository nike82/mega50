# def get_todos(file_path="./files/todos.txt"):
#     """ Read a text file and return the list of
#     to-do items.
#     """
#     with open(file_path, "r") as file_local:
#         todos_local = file_local.readlines()
#     return todos_local
#
#
# def write_todos(todos_arg, file_path="./files/todos.txt"):
#     """ Write the to-do items in the tex file."""
#     with open(file_path, "w") as file_local:
#         file_local.writelines(todos_arg)
#
# text = """
# First line,
# Second line,
# Third line
# """
#
# print(text)
#
# while True:
#     user_action = input("Type add, show, edit, complete or exit: ")
#     user_action = user_action.strip()
#
#     if user_action.startswith("add"):
#         todo = user_action[4:]
#         todos = get_todos()
#         todos.append(todo + "\n")
#
#         write_todos(todos)
#
#     elif user_action.startswith("show"):
#         todos = get_todos()
#         for index, item in enumerate(todos):
#             item = item.strip("\n")
#             print(f"{index + 1}-{item}")
#
#     elif user_action.startswith("edit"):
#         try:
#             number = int(user_action[5:])
#             number = number - 1
#             todos = get_todos()
#             new_todo = input("Enter new todo: ")
#             todos[number] = new_todo + "\n"
#             write_todos(todos)
#         except ValueError:
#             print("Your command is not valid!")
#             continue
#
#     elif user_action.startswith("complete"):
#         try:
#             number = int(user_action[9:])
#             todos = get_todos()
#             index = number - 1
#             todo_to_remove = todos[index].strip("\n")
#             todos.pop(index)
#             write_todos(todos)
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

# def get_average():
#     with open("./files/data.txt", "r") as file:
#         data = file.readlines()
#     values = data[1:]
#     values = [float(i) for i in values]
#     average_local = sum(values) / len(values)
#     return average_local
#
#
# average = get_average()
# print(average)

feet_inches = input("Enter feet and inches: ")


def parse(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meters = feet * 0.3048 + inches + 0.0254
    return meters


parsed = parse(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("Kid is too small!")
else:
    print("Kid can use the slide!")