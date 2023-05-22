# Task 5: Implement/code the User.get_name method,
# so the method returns the capitalized version of the user's name (e.g., JOHN).
# Note that the name is stored in the instance variable. Also, call the method for the instance you created in Task 4.
# Solution: See the attached task5.py file in the Resources of the next lecture.

class User:

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        return self.name.upper()

    def get_age(self, current_year):
        return current_year - self.birth_year


user_john = User("john", 1999)
print(user_john.get_age(2023))
print(user_john.get_name())
