# toDoApp.py
"""
A simple To-Do List Application.
Features:
- Add task
- Show tasks
- Remove task
"""

tasks = []

def addtask(task):
    if not task.strip():
        print("Task cannot be empty!")
    else:
        tasks.append(task.strip())
        print("Task added!")

def showTasks():
    if len(tasks) == 0:
        print("No tasks yet.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def removetask(tasknumber):
    if 1 <= tasknumber <= len(tasks):
        removed = tasks.pop(tasknumber - 1)
        print(f"Task removed: {removed}")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            t = input("Enter task: ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                try:
                    n = int(input("Enter task number to remove: "))
                    removetask(n)
                except ValueError:
                    print("Please enter a valid number!")
        elif ch == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again!")

if __name__ == "__main__":
    main()
