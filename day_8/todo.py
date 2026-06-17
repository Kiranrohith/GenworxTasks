import datetime
from tabulate import tabulate
todolist = []
task_id = 0

def add_task():
    try:
        global task_id
        task_id += 1
        task = input("Enter the task: ").strip()
        if not task:
            print("Error: Task description cannot be empty.\n")
            task_id -= 1
            return
        time = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
        end_time = ""
        task_list = [task_id, task, time, "Pending", end_time]
        todolist.append(task_list)
        print("Task added!\n")
    except KeyboardInterrupt:
        print("\nTask addition cancelled.\n")
        task_id -= 1
    except Exception as e:
        print(f"Error adding task: {e}\n")
        task_id -= 1

def complete_task():
    try:
        list_tasks()
        if not todolist:
            print("No tasks to finish.\n")
            return
        
        try:
            task_ids = int(input("Enter the task number to finish: "))
            if 1 <= task_ids <= len(todolist):
                todolist[task_ids - 1][3] = "Completed"
                todolist[task_ids - 1][4] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                print("Task finished\n")
            else:
                print(f"Invalid task number! Please enter a number between 1 and {len(todolist)}\n")
        except ValueError:
            print("Error: Please enter a valid numeric task number.\n")
    except KeyboardInterrupt:
        print("\nTask completion cancelled.\n")
    except Exception as e:
        print(f"Error completing task: {e}\n")

def list_tasks():
    if not todolist:
        print("No tasks yet.\n")
        return
    header = ["Id","Task","Creation time","Status","Completion time"]
    
    print(tabulate(todolist, headers=header, tablefmt="pretty", numalign="left", stralign="left"))
def task_modifier():
    try:
        while True:
            try:
                print("\n1.Add task\n2.Complete task\n3.List tasks\n4.Close")
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
                        print("Exiting todo list.\n")
                        break
                    case _:
                        print("Wrong input! Please enter a number between 1 and 4.\n")
            except ValueError:
                print("Error: Please enter a valid number.\n")
            except KeyboardInterrupt:
                print("\nMenu navigation cancelled.\n")
    except Exception as e:
        print(f"Error in todo menu: {e}\n")