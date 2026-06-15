import datetime
from tabulate import tabulate
todolist = []
task_id = 0

def add_task():
    global task_id
    task_id+=1
    task = input("Enter the task: ")
    time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
    end_time = 00-00-00
    task_list = [task_id,task,time,"Pending",end_time]
    todolist.append(task_list)
    print("Task added!\n")

def complete_task():
    list_tasks()
    if not todolist:
        print("No tasks to finish.\n")
        return
    
    task_ids = int(input("Enter the task number to finish: "))
    if 1 <= task_ids <= len(todolist):
        todolist[task_ids-1][3] = "Completed"
        todolist[task_ids-1][4] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print("Task finished\n")
    else:
        print("Invalid task number!\n")

def list_tasks():
    if not todolist:
        print("No tasks yet.\n")
        return
    header = ["Id","Task","Creation time","Status","Completion time"]
    
    print(tabulate(todolist, headers=header, tablefmt="pretty", numalign="left", stralign="left"))

while(True):
    print("\n1.Add task\n2.complete task\n3.List tasks\n4.Close")
    choice = input("Select an option: ").strip()
    if not choice.isdigit():
        print("Invalid input: please enter a number between 1 and 4.\n")
        continue
    user_choice = int(choice)
    match user_choice:
        case 1:
            add_task()
        case 2:
            complete_task()
        case 3:
            list_tasks()
        case 4:
            break;
        case _:
            print("Wrong input !!")