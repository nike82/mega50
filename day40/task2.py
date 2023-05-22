# Task 2: Add an __init__ method to the User class. The method should have:
# 1. three parameters, self, name, and birth_year.
# 2. name and birth_year should also be instance variables.
# Solution:  See the attached task2.py file in the Resources of the next lecture.

class User:
    def __int__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def get_name(self):
        pass

    def get_age(self, current_year):
        pass