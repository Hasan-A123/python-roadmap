# ====================================
# Project 5 - To-Do List
# Python Roadmap
# Simple To Do List Application
# Allows users to add, view, and remove tasks
# ====================================


def main():

    tasks = []
    while True:
        print("\n===== TO-DO LIST =====")
        print(f"Tasks: {len(tasks)}")
        print("\n")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        print("\n Choose an option: ")

        # Add Task
        choice = int(input("What is your choice? "))
        if choice == 1:
            print("\nAdd a new task")
            
            task = input("Enter a task: ")
            if task == "":
                print("Empty task not allowed")
                continue
            if task in tasks:
                print("Task already exists")
                continue
            
            tasks.append(task)
            print(f'"{task}" added successfully!')

        # View Tasks
        elif choice == 2:
            if len(tasks) == 0:
                print("No tasks found")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")


        # Remove Task
        elif choice == 3:
            if len(tasks) == 0:
                print("No tasks to remove")
            else:
                print("\nYour tasks:")
                for i, task in enumerate(tasks):
                    print(f"{i + 1}. {task}")
                task_number = int(input("Enter task number to remove: "))
                task_index = (task_number) - 1
                if 0 <= task_index < len(tasks):
                    ask_user = input("Are you sure? (yes/no): ").lower()
                    if ask_user == "yes":
                        removed_task = tasks.pop(task_index)
                        print(f"Removed: {removed_task}")
                    else:
                        print("Cancelled")
                else:
                    print("Invalid task number")
                



        elif choice == 4:
            print("Goodbye")
            break
        else:
            print("Invalid option. Please choose 1-4")



if __name__ == "__main__":
    main()
