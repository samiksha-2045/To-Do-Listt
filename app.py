
# To-Do List Application
tasks = []

def add_task():
    task = input("Enter your task: ")

    tasks.append({
        "task": task,
        "completed": False
    })

    print("Task added successfully!")


def view_tasks():
    if not tasks:
        print("\nYour task list is empty!")
    else:
        print("\n------- YOUR TO-DO LIST -------")

        for i, task in enumerate(tasks, start=1):

            if task["completed"]:
                status = "Completed"
            else:
                status = "Pending"

            print(f"{i}. {task['task']} - {status}")


def update_task():
    view_tasks()

    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number to update: "))

        if 1 <= choice <= len(tasks):
            new_task = input("Enter the new task: ")

            tasks[choice - 1]["task"] = new_task

            print("Task updated successfully!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number to delete: "))

        if 1 <= choice <= len(tasks):
            removed_task = tasks.pop(choice - 1)

            print("Task deleted:", removed_task["task"])
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


def complete_task():
    view_tasks()

    if not tasks:
        return

    try:
        choice = int(input("\nEnter task number to mark as completed: "))

        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True

            print("Task marked as completed!")
        else:
            print("Invalid task number!")

    except ValueError:
        print("Please enter a valid number!")


# Main Program

while True:

    print("\n========== TO-DO LIST APPLICATION ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Completed")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        update_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        complete_task()

    elif choice == "6":
        print("\nThank you for using the To-Do List Application!")
        break

    else:
        print("Invalid choice! Please select between 1 and 6.")
