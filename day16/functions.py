FILE_PATH = "./files/todos.txt"


def get_todos(file_path=FILE_PATH):
    """ Read a text file and return the list of
    to-do items.
    """
    with open(file_path, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, file_path=FILE_PATH):
    """ Write the to-do items in the tex file."""
    with open(file_path, "w") as file_local:
        file_local.writelines(todos_arg)


def count(phrase):
    return phrase.count('.')


if __name__ == "__main__":
    print("hello from here!")
