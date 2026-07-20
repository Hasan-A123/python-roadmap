# ====================================
# Project 5 - To-Do List
# Python Roadmap
# Simple To-Do List Application
# Allows users to add, view, and remove tasks
# ====================================


def main():

    # List to store tasks
    tasks = []

    while True:

        # =========================
        # Main Menu
        # =========================
        print("\n===== TO-DO LIST =====")
        print(f"Tasks: {len(tasks)}")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("\nChoose an option: ")

        # =========================
        # Add Task
        # =========================
        if choice == "1":
            print("\nAdd a new task")

            # Get task from the user
            task = input("Enter a task: ").strip()

            # Validate task input
            if task == "":
                print("Empty task not allowed")
                continue

            # Prevent duplicate tasks
            if task in tasks:
                print("Task already exists")
                continue

            # Add task to the list
            tasks.append(task)
            print(f'"{task}" added successfully!')

        # =========================
        # View Tasks
        # =========================
        elif choice == "2":

            if len(tasks) == 0:
                print("No tasks found")
            else:
                print("\nYour tasks:")

                # enumerate() gives each task a number
                # start=1 makes numbering begin at 1
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        # =========================
        # Remove Task
        # =========================
        elif choice == "3":

            if len(tasks) == 0:
                print("No tasks to remove")
            else:
                print("\nYour tasks:")

                # Display tasks with numbered positions
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

                # Ask the user which task to remove
                task_number = int(input("Enter task number to remove: "))

                # Lists use zero-based indexes,
                # so subtract 1 from the user's number
                task_index = task_number - 1

                # Check that the index is valid
                if 0 <= task_index < len(tasks):

                    # Confirm before removing the task
                    ask_user = input(
                        "Are you sure? (yes/no): "
                    ).lower()

                    if ask_user == "yes":

                        # pop() removes and returns the task
                        removed_task = tasks.pop(task_index)

                        print(f"Removed: {removed_task}")

                    else:
                        print("Cancelled")

                else:
                    print("Invalid task number")

        # =========================
        # Exit Program
        # =========================
        elif choice == "4":
            print("Goodbye")
            break

        # =========================
        # Invalid Menu Option
        # =========================
        else:
            print("Invalid option. Please choose 1-4")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()