def read_todo(filename="todo.txt"):
    with open(filename , "r") as file:
        my_todo = file.readlines()
    return my_todo


def write_todo(todos , filename="todo.txt"):
    with open(filename , "w") as file:
        file.writelines(todos)


# name = file of name (functions) ...toh in functions it will show "main" but todoCLI mein it will show filename (functions)
# __name__ is a string
if __name__ == "__main__": #imported file mein yeh print statement wont be run
    print("this is a test line")
