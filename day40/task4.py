# Task 4: Let us suppose the current year is 2023.
# 1. Create a User instance for John, whose birth year is 1999.
# 2. Call the age method for that instance and print out the output.
# You should get 24 as output.
# Solution: See the attached task4.py file in the Resources of the next lecture.

class User:

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        pass

    def get_age(self, current_year):
        return current_year - self.birth_year


user_john = User("John", 1999)
print(user_john.get_age(2023))

