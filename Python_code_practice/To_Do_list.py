from random import choice

from scipy.__config__ import show


task=[]
def show_menu():
   print( "1. Add the task\n")
   print( "2. Show the task\n")
   print( "3. Delete the task\n")
   print( "4. Exit\n")
def task_add():
    task_input=input(str(" Enter the Task:\n"))
    task.append(task_input)
def task_show():
    if task is None:
        print("No task")
    else:
        for i in range(len(task)):
            print(i+1,task[i],"\n")

def task_delete():
    task_delete=input(str("Enter the task to be deleted: \n"))
    task.remove(task_delete)
    print(task)

while True:
    show_menu()
    choices=input("Enter the number to select the task:\n")
    if choices=="1":
        task_add()
    elif choices=="2":
        task_show()
    elif choices=="3":
        task_delete()
    elif choices=="4":
        print("Exit")
        break
    