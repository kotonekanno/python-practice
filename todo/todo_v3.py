#締め切りと優先順位を追加できる
#編集できる

tasks = []
from datetime import datetime

def show_menu():
    print("\n====  ToDo Menu ====")
    print("1: Add Task")
    print("2: Show Tasks")
    print("3. Edit task")
    print("4: Delete Task")
    print("5: Exit")

def add_task():
    try:
        task = {}
        task["title"] = input("\nEnter a task: ")
        deadline = input("Enter the deadline (YYYY-MM-DD): ")
        task["deadline"] = datetime.strptime(deadline,"%Y-%m-%d").date()
        
        print("\n1. Very High")
        print("2. High")
        print("3. Medium")
        print("4. Low")
        print("5. Very Low")
        task["priority"] = int(input("Choose the priority: "))
        
        if(task["priority"] < 1 or 5 < task["priority"]):
            raise ValueError
        else:
            tasks.append(task)
            print(f"\n'{task['title']}' added!")
            print(f"The deadline is {task['deadline']}!")
    
    except ValueError:
        print("\nInvalid number.")

def enumerate_tasks():
        if not tasks: print("\nno tasks.")
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

def show_tasks():
    enumerate_tasks()

    print("\n1. Sort tasks")
    print("2. Exit")
    choice = input("Choose an option: ")

    if choice == '1': sort()
    elif choice == '2': print()
    else:
        print("\nInvalid number.")
        show_tasks()

def edit_task():
    enumerate_tasks()
    
    try:
        num = int(input("\nEnter task number: "))
        print(F"\n{tasks[num-1]['title']}  {tasks[num-1]['deadline']}")
        print("\n1. Edit title")
        print("2. Change deadline")
        print("3. Change priority")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            tasks[num-1]["title"] = input("\nEnter a task: ")
            print(F"\nUpdated to '{tasks[num-1]['title']}'!")
            edit_task()
        elif choice == '2':
            deadline = input("\nEnter the deadline (YYYY-MM-DD): ")
            tasks[num-1]["deadline"] = datetime.strptime(deadline,"%Y-%m-%d").date()
            print(F"\nThe deadline is {tasks[num-1]['deadline']}!")
            edit_task()
        elif choice == '3':
            print("\n1. Very High")
            print("2. High")
            print("3. Medium")
            print("4. Low")
            print("5. Very Low")
            tasks[num-1]["priority"] = int(input("Choose the priority: "))
            if(tasks[num-1]["priority"] < 1 or 5 < tasks[num-1]["priority"]):
                raise ValueError
        elif choice == '4': edit_task()
            
        else: raise ValueError
    
    except(ValueError,IndexError):
        print("\nInvalid number.")
        edit_task()

def delete_task():
    enumerate_tasks()
    try:
        num = int(input("\nEnter task number: "))
        removed = tasks.pop(num-1)
        print(F"\n'{removed['title']}' deleted!")
    except(ValueError, IndexError):
        print("\nInvalid number.")
        delete_task()

while True:
    show_menu()
    choice = input("\nChoose an option: ")
    if choice == '1': add_task()
    elif choice == '2': show_tasks()
    elif choice == '3': edit_task()
    elif choice == '4': delete_task()
    elif choice == '5':
        print("\nBye!")
        break
    else:
        print("\nInvalid choice.")
