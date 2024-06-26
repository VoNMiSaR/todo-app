import functions
import time

now = time.strftime("%b %d, %H:%M:%S")

print("The time now is: ", now)

while True:
    user_action = input("To-do List: Add, Show, Complete or Exit: ")
    user_action = user_action.strip().lower()

    if user_action.startswith("add"):
        todos = functions.get_todos()

        todo = user_action[4:] + "\n"
        todos.append(todo.capitalize())

        functions.set_todos(todos)

    if user_action.startswith("show"):
        todos = functions.get_todos()

        new_todos = [item.strip("\n") for item in todos]

        for index, item in enumerate(new_todos):
            print(f"{index + 1}-{item}")

    if user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            index = number - 1

            todos = functions.get_todos()

            new_to_do = input("Replace " + todos[index] + " with?: ")
            todos[index] = new_to_do.capitalize() + "\n"

            functions.set_todos(todos)

            print("Done!")
        except ValueError:
            print("Unexpected Value Encountered. Enter the number of todo to edit.")
            continue

    if user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            index = number - 1

            todos = functions.get_todos()

            removed_todo = todos.pop(index).strip("\n")
            print(f"'{number}-{removed_todo}' Marked as Completed and removed from to-do list")

            functions.set_todos(todos)
        except IndexError:
            print("Todo number out of range. Enter appropriate todo number.")
            continue

    if user_action.startswith("exit"):
        print("Goodbye!")
        break

    # else:
    #    print("That command does not exist!")
