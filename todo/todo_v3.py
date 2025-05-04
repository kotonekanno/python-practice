#締め切りと優先順位を追加できる
#編集できる

tasks = []
from datetime import datetime

def show_menu():
    print("\n====  ToDo Menu ====")
    print("1: Add Task")
    print("2: Show Tasks")
    print("3. Edit Task")
    print("4: Delete Task")
    print("5: Exit")

def add_task():
    task = {}
    print("999 to Cancel")
    task["title"] = input("\nEnter a task: ")
    
    if task["title"] == "999": print()
    
    else:
        task['deadline'] = ()
        task['deadline'] = set_deadline()

        task['priority'] = 5
        task['priority'] = prioritize()
        match task['priority']:
            case 1: str_a = ("Very High")
            case 2: str_a = ("High")
            case 3: str_a = ("Medium")
            case 4: str_a = ("Very Low")
            case 5: str_a = ("Low")
        
        tasks.append(task)
        print(f"\n'{task['title']}' added!")
        print(f"The deadline is {task['deadline']}!")
        print(f"The priority is '{str_a}'!")

def set_deadline():
    try:
        deadline_pre = input("Enter the deadline (YYYY-MM-DD): ")
        deadline = datetime.strptime(deadline_pre,"%Y-%m-%d").date()
        return deadline
    
    except ValueError:
        print("\nInvalid number.")
        return set_deadline()

def prioritize():
    try:
        print("\n1. Very High")
        print("2. High")
        print("3. Medium")
        print("4. Low")
        print("5. Very Low")
        priority = int(input("Choose the priority: "))
        
        if(priority < 1 or 5 < priority): raise ValueError
        return priority

    except ValueError:
        print("\nInvalid number.")
        return prioritize()

def show_tasks():
    enumerate_tasks()

    print("\n--- Menu ---")
    print("1. Sort tasks")
    print("2. Exit")
    choice = input("Choose an option: ")

    if choice == '1': sort()
    elif choice == '2': print()
    else:
        print("\nInvalid number.")
        show_tasks()

def enumerate_tasks():
    if not tasks: print("\nNo tasks.")

    else:
        print("\nTasks:")
        today = datetime.now().date()

        for i, task in enumerate(tasks,1):
            print(f"{i}.{task['title']}  {task['deadline']}")

            if task["deadline"] < today:
                print("  Expired!")
            
            else:
                time_left = task["deadline"] - today
                print(" ",time_left.days,"days left!")

def sort():
    print("\n1. Sort by date")
    print("2. Sort by priority")
    print("3. Cancel")
    choice = input("Choose an option: ")
    
    if choice == '1':
        tasks.sort(key=lambda x: x["deadline"])
        show_tasks()
    
    elif choice == '2':
        tasks.sort(key=lambda x: x["priority"])
        show_tasks()
    
    elif choice == '3': show_tasks()
    
    else:
        print("\nInvalid number.")
        show_tasks()

def edit_task(num_e):
    if num_e == 0:
        enumerate_tasks()
        print("\n999. Exit")
        num_e2 = int(input("\nEnter task number: "))
        edit_task(num_e2)
    
    else:
        try:
            if num_e == 999: print()

            else:
                print(F"\n{tasks[num_e-1]['title']}  {tasks[num_e-1]['deadline']}")
                print("\n1. Edit title")
                print("2. Reset deadline")
                print("3. Change priority")
                print("4. Exit")
                choice = input("Choose an option: ")

                if choice == '1':
                    tasks[num_e-1]["title"] = input("\nEnter a task: ")
                    print(F"\nUpdated to '{tasks[num_e-1]['title']}'!")
                    edit_task(num_e)
                
                elif choice == '2':
                    tasks[num_e-1]['deadline'] = set_deadline()
                    print(f"\nUpdated to {tasks[num_e-1]['deadline']}!")
                    edit_task(num_e)
                
                elif choice == '3':
                    tasks[num_e-1]['priority'] = prioritize()
                    match tasks[num_e-1]['priority']:
                        case 1: str_p = ("Very High")
                        case 2: str_p = ("High")
                        case 3: str_p = ("Medium")
                        case 4: str_p = ("Very Low")
                        case 5: str_p = ("Low")
                    print(f"Updated to '{str_p}'!")
                    edit_task(num_e)
                
                elif choice == '4': edit_task(0)
                    
                else: raise ValueError
        
        except(ValueError,IndexError):
            print("\nInvalid number.")
            edit_task(0)    

def delete_task():
    enumerate_tasks()

    try:
        print("\n999 to cancel")
        num = int(input("Enter task number: "))

        if num == 999: print()

        else:
            removed = tasks.pop(num-1)
            print(F"\n'{removed['title']}' deleted!")
    
    except(ValueError, IndexError):
        print("\nInvalid number.")
        delete_task()

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1': add_task()
    elif choice == '2': show_tasks()
    elif choice == '3': edit_task(0)
    elif choice == '4': delete_task()
    elif choice == '5':
        print("\nBye!")
        break
    
    else:
        print("\nInvalid choice.")