tasks = []

def addtask(task):
    tasks.append(task)
    print("task added!")

def showTasks():
    if len(tasks) == 0:
        print("no tasks yet")
    else:
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])

def removetask(tasknumber):
    if tasknumber < 1 or tasknumber > len(tasks):
        print("Invalid task number. Please try again.")
    else:
        tasks.pop(tasknumber - 1) 
        print("task removed!!")

def main():
    while True:
        print("\n1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        ch = input("enter choice: ")

        if ch == "1":
            t = input("enter task: ")
            addtask(t)

        elif ch == "2":
            showTasks()

        elif ch == "3":
            if len(tasks) == 0:
                print("No tasks to remove.")
            else:
                try:
                    n = int(input("enter task no to remove: "))
                    removetask(n)
                except ValueError:
                    print("Please enter a valid number.")

        elif ch == "4":
            break

        else:
            print("wrong choice!")

main()
