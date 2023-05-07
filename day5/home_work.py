
###########################
# Coding Exercise 1
# filenames = ['document', 'report', 'presentation']
#
# Copy-paste the above list in a .py file and extend the code,
# so it prints out the output below:
#
# 0-Document.txt
# 1-Report.txt
# 2-Presentation.txt

filenames = ['document', 'report', 'presentation']
filenames.sort()
for index, item in enumerate(filenames):
    print(f'{index}-{item.capitalize()}.txt')

#########################################
# Coding Exercise 2
# ips = ['100.122.133.105', '100.122.133.111']
#
# Copy-paste the ips list in a .py file and extend the program so it:
#
# 1. Prompts the user to input an index (e.g, 0 or 1).
#
# 2. Returns the IP address that has that index.

ips = ['100.122.133.105', '100.122.133.111']

index = int(input("Input index (e.g, 0 or 1): "))
print(f'You choose {ips[index]}')

######################################
# Bug-Fixing Exercise 1
# Supposedly, the following program should:
#
# 1. Prompt the user to input an index (e.g., 0, 1, or 2).
#
# 2. Print out the item with that index.
#
# However, there is a bug with the program which you should try to fix.
#
# menu = ["pasta", "pizza", "salad"]
#
# user_choice = input("Enter the index of the item: ")
#
# message = f"You chose {menu[user_choice]}."
# print(message)

menu = ["pasta", "pizza", "salad"]
user_choice = int(input("Enter the index of the item: "))
message = f"You chose {menu[user_choice]}."
print(message)

###################################
# Bug-Fixing Exercise 2
# Here is another piece of buggy code:
#
# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate[menu]:
#     print(f"{i}.{j}")

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")

######################################
# Bug-Fixing Exercise 3
# Here is another piece of code that contains a bug:
#
# menu = ["pasta", "pizza", "salad"]
#
# for i, j in enumerate(menu):
#     print("f{i}.{j}")

menu = ["pasta", "pizza", "salad"]

for i, j in enumerate(menu):
    print(f"{i}.{j}")
