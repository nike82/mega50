todos = []
while True:
    user_action = (input("Type add, show, edit or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                print(item)
        case 'edit':
            number = int(input("Number of te todo to edit: "))
            number -= number
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
            print(todos)
        case 'exit':
            break
        case default:
            print("Don't be an idiot, print correct!")

print("fuck off asshole!")

# Bonus
filenames = ["1.Raw Data.txt", "2.Reports.txt", "3.Presentations.txt"]

for filename in filenames:
    filename = filename.replace('.', '-', 1)
    print(filename)

