
# while True:
#     user_action = input("Throw the coin and enter head or tail ?: ")
#     with open("files/coin-flip.txt", "r") as file:
#         content = file.readlines()
#
#     content.append(user_action + "\n")
#
#     result = str(content.count("head\n") * 100 / len(content))
#     print(f"Heads: {result}%")
#
#     with open("files/coin-flip.txt", "w") as file:
#         file.writelines(content)


#########################
# # Bonus
# date = input("Enter today's date: ")
# mood = input("How do you rate your mood today from 1 to 10? ")
# thoughts = input("Let your thoughts flow: \n")
#
# with open(f"./journal/{date}.txt", "w") as file:
#     file.write(mood + 2 * "\n")
#     file.write(thoughts)


# Bug-Fixing Exercise 1
# with open("file.txt", 'r') as file:
#     print(file.read())
#     print(len(file.read()))
# The Python script above is in the same directory with a file named file.txt whose content is:
#
# Hello You
#
# The Python script should print out the content of the file and the number of characters of the text inside file.txt.
# So, the expected output would be:
#
# Hello You
# 9
# However, the script prints out this:
#
# Hello You
# 0
# Can you fix the program, so it prints out the expected output?

with open("file.txt", 'r') as file:
    content = file.read()
    print(content)
    print(len(content))
