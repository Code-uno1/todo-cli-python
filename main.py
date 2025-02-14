print("Welcome to the To-Do List App!")
print("1. Add a task")
print("2. View tasks")
print("3. Delete a task")
choice = input("Enter your choice (1, 2, or 3): ")

if choice == "1":
    task = input("Enter a task: ")
    with open("todo.txt", "a") as file:
        file.write(task + "\n")
    print(f"Task '{task}' added successfully!")

elif choice == "2":
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks found!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")

    except FileNotFoundError:
        print("No tasks found!")

elif choice == "3":
    try:
        with open("todo.txt", "r") as file:
            tasks = file.readlines()

        if not tasks:
            print("No tasks to delete!")
        else:
            print("\nYour Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task.strip()}")

            task_num = int(input("Enter the task number to delete: ")) - 1

            if 0 <= task_num < len(tasks):
                deleted_task = tasks.pop(task_num)  # Remove from list
                with open("todo.txt", "w") as file:  # Overwrite file
                    file.writelines(tasks)
                print(f"Task '{deleted_task.strip()}' deleted successfully!")
            else:
                print("Invalid task number!")

    except FileNotFoundError:
        print("No tasks found!")

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
