
todos = []

while True:
    user_action = (input("Type add or show, or exit: ")).strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'display':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case default:
            print("Don't be an idiot, print correct!")

print("fuck off asshole!")

# Bonus
meals = ['pasta', 'pizza', 'salad']

for meal in meals:
    print(meal.capitalize())

for char in 'meals':
    print(char.capitalize())

print("Fuck off!")
