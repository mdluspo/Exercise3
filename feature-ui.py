#feature-ui
tasks=[]

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
        print("1 Add Task")
        print("2.Show Tasks")
        print("3.Remove Task")
        print("4.Exit")
        ch = input("Enter number of action to execute: ")
        if ch=="1":
            t = input("Enter task : ")
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