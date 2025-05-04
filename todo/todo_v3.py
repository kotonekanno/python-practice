#締め切りと優先順位を追加できる

tasks = []
from datetime import datetime

def show_menu():
    print("\n====  ToDo Menu ====")
    print("1: Add Task")
    print("2: Show Tasks")
    print("3: Delete Task")
    print("4: Exit")

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
    choice_st_s = input("Choose an option: ")
    
    if choice_st_s == '1':
        tasks.sort(key=lambda x: x["deadline"])
        show_tasks()
    elif choice_st_s == '2':
        tasks.sort(key=lambda x: x["priority"])
        show_tasks()
    elif choice_st_s == '3': show_tasks()
    else:
        print("\nInvalid number.")
        show_tasks()

def show_tasks():
    enumerate_tasks()

    print("\n1. Sort tasks")
    print("2. Exit")
    choice_st = input("Choose an option: ")

    if choice_st == '1': sort()
    elif choice_st == '2': print()
    else:
        print("\nInvalid number.")
        show_tasks()

def delete_task():
    enumerate_tasks()
    try:
        num = int(input("\nEnter task number: "))
        removed = tasks.pop(num-1)
        print(F"\n'{removed['title']}' deleted!")
    except (ValueError, IndexError):
        print("\nInvalid number.")

while True:
