todos = []
while True:
    user_action = (input("Type add, show, edit, complete or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for index, item in enumerate(todos):
                print(f'{index + 1}-{item}')
        case 'edit':
            number = int(input("Number of te todo to edit: "))
            number -= number
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Numbers of todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case default:
            print("Don't be an idiot, print correct!")

print("fuck off asshole!")

#########################
# Bonus
waiting_list = ["sen", "ben", "john"]
waiting_list.sort()

for index, item in enumerate(waiting_list):
    row = f"{index}.{item.capitalize()}"
    print(row)

waiting_list.sort(reverse=True)
print(waiting_list)