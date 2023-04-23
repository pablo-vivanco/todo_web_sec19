import os

FILEPATH='todos.txt'


def list_todos(todos):
    """
    Prints a numbered list of todos to the console.

    Args:
    todos (list): A list of strings containing the todos to be printed.

    Returns:
    None
    """
    
    for ind, td in enumerate(todos):
        print(f'\t{ind+1:2d}: {td}')

def load_todos(filepath=FILEPATH):
    """
    Reads a file containing a list of todos and returns them as a list of strings.

    Args:
    filepath (str, optional): The path to the file containing the todos. Default is FILEPATH.

    Returns:
    list: A list of strings containing the todos read from the file.
    """
    if not os.path.exists(filepath):
        # create an empty file
        with open(filepath,'w') as file:
            pass

    with open(filepath,'r') as file:
        todos = file.read().splitlines()

    return todos

def save_todos(todos, filepath=FILEPATH):
    """
    Writes a list of todos to a file.

    Args:
    todos (list): A list of strings containing the todos to be saved.
    filepath (str, optional): The path to the file where the todos will be saved. Default is 'todos.txt'.

    Returns:
    None
    """
    with open(filepath,'w') as file:
        file.write('\n'.join(todos))
