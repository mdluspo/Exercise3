"""
This is a simple to-do list application.
It allows users to add, view, and remove tasks from their to-do list.
The application runs in a loop, presenting a menu of options to the user until they choose to exit.
The tasks are stored in a list, and the user can interact with the application through console input.
"""
tasks = []

def add_task(task):
    if not task.strip():
        print("Task cannot be empty!")
    else:
        tasks.append(task.strip())
        print("Task added!")

def show_tasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task(task_number):
    if 1 <= task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Task removed: {removed}")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("=======================================")
        print(">>> TO DO MENU: <<<")
        print("   1.Add Task")
        print("   2.Show Tasks")
        print("   3.Remove Task")
        print("   4.Exit")
        choice = input("Enter number of action to execute: ")
        print("=======================================")

        if choice == "1":
            opt = input("Enter task: ")
            add_task(opt)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                try:
                    delete = int(input("Enter task number to remove: "))
                    remove_task(delete)
                except ValueError:
                    print("Please enter a valid number!")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()