tick = "\u2714"  # ✔ Tick Mark
unchecked = "[ ]"
checked = f"[{tick}]"  # [✔]

def add_task():
    """Adds a new task to tasks.txt"""
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(f"{unchecked} {task}\n")
    print("Task added successfully!")

def display_tasks():
    """Displays tasks in a neat format"""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if not tasks:
            print("No tasks available!")
            return

        print("\n📋 Your Task List:")
        for index, task in enumerate(tasks, start=1):
            task = task.strip()
            icon = "✅" if checked in task else "📌"
            print(f"{icon} {index}. {task}")

    except FileNotFoundError:
        print("No tasks found! Add some first.")

def mark_task_done():
    """Marks a task as completed in tasks.txt"""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if not tasks:
            print("No tasks found!")
            return

        display_tasks()  # Show tasks before asking

        try:
            task_num = int(input("\nEnter task number to mark as done: ")) - 1
            if 0 <= task_num < len(tasks):
                if checked in tasks[task_num]:
                    print("Task is already marked as done! ✅")
                else:
                    tasks[task_num] = tasks[task_num].replace(unchecked, checked)

                    with open("tasks.txt", "w") as file:
                        file.writelines(tasks)

                    print("Task marked as done! ✅")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

    except FileNotFoundError:
        print("No tasks found! Add some first.")

def delete_task():
    """Deletes a task from tasks.txt"""
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        
        if not tasks:
            print("No tasks to delete!")
            return

        display_tasks()  # Show tasks before asking

        try:
            task_num = int(input("\nEnter task number to delete: ")) - 1
            if 0 <= task_num < len(tasks):
                deleted_task = tasks.pop(task_num)

                with open("tasks.txt", "w") as file:
                    file.writelines(tasks)

                print(f"Deleted: {deleted_task.strip()}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

    except FileNotFoundError:
        print("No tasks found! Add some first.")

def menu():
    """Simple menu for task management"""
    while True:
        print("\n📋 To-Do List App")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            mark_task_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice! Try again.")

# Call the menu to start the app
menu()
