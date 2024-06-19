def get_todos(filepath="todo.txt"):
    with open(filepath, "r") as file:
        read_file = file.readlines()
    return read_file


def set_todos(todos_local, filepath="todo.txt"):
    with open(filepath, "w") as file:
        file.writelines(todos_local)


if __name__ == "__main__":
    print(get_todos())
