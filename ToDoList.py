FILENAME = "Tasks.txt"

def add_task():
    task = input("Enter Task: ")
    date = input("Enter Date: ")
    time = input("Enter Time (a.m or p.m): ")
    with open(FILENAME, "a") as file:
        file.write(f"{task},{date},{time}\n")
        print("✅ Task added successfully.\n")


def view_task():
    print("\n📋 To-Do List:")
    with open(FILENAME, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No tasks found.")
            return
        for i, line in enumerate(lines, start=1):
            if line.strip():
                try:
                    task, date, time = line.strip().split(",")
                    print(f"{i}. Task: {task} | Date: {date} | Time: {time}")
                except ValueError:
                    print(f"{i}. ⚠️ Skipping malformed task: {line.strip()}")


def mark_complete():
    view_task()
    try:
        task_num = int(input("\nEnter the task number to mark as complete: "))
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        if 1 <= task_num <= len(lines):
            lines[task_num - 1] = "[✓] " + lines[task_num - 1]
            with open(FILENAME, "w") as file:
                file.writelines(lines)
            print(" Task marked as complete.\n")
        else:
            print(" Invalid task number.\n")
    except ValueError:
        print(" Please enter a valid number.\n")


def delete_task():
    view_task()
    try:
        task_num = int(input("\nEnter the task number to delete: "))
        with open(FILENAME, "r") as file:
            lines = file.readlines()

        if 1 <= task_num <= len(lines):
            deleted = lines.pop(task_num - 1)
            with open(FILENAME, "w") as file:
                file.writelines(lines)
            print(f" Deleted task: {deleted.strip()}")
        else:
            print(" Invalid task number.\n")
    except ValueError:
        print(" Please enter a valid number.\n")


def menu():
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            mark_complete()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print(" Goodbye!")
            break
        else:
            print(" Invalid option. Please enter 1–5.\n")


# Start the app
menu()
