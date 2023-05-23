# Task 3: Implement/code the User.get_age method so the method returns
# the age of the user given the self.birth_year instance variable and the current_year parameters.
# Solution:  See the attached task3.py file in the Resources of the next lecture.

class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        pass

    def get_age(self, current_year):
        return current_year - self.birth_year
