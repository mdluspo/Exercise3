#feature-ui

tasks=[]

"""
This is a simple to-do list application.
It allows users to add, view, and remove tasks from their to-do list.
The application runs in a loop, presenting a menu of options to the user until they choose to exit.
The tasks are stored in a list, and the user can interact with the application through console input.
"""

def addtask(task) :
    tasks.append(task)
    print("task added!")

def showTasks( ):
    if len(tasks)==0 :
        print("no tasks yet")
    else:
        for i in range (len(tasks)):
            print(i+1,".",tasks[i])
      
def removetask(tasknumber):
    tasks.pop(tasknumber) 
    print("Task removed!!")

def main():
    while True:
        print("=======================================")
        print(">>> TO DO MENU: <<<")
        print("   1.Add Task")
        print("   2.Show Tasks")
        print("   3.Remove Task")
        print("   4.Exit")
        ch = input("Enter number of action to execute: ")
        print("=======================================")
        if ch=="1":
            t = input("Enter task: ")
            addtask(t)
        elif ch=="2":
            print("Here's the list of your tasks:\n")
            showTasks()
        elif ch=="3":
            n = int(input("Enter task no to remove: "))
            removetask(n)   
        elif ch=="4":
            break;
        else:
            print("Invalid input!!")
main()