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

def prioritize():
    tasks.sort(key=lambda x: x["priority"])

def show_tasks():
    prioritize()
    if not tasks:
        print("\nno tasks.")
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

def delete_task():
    show_tasks()
    try:
        num = int(input("\nEnter task number: "))
        removed = tasks.pop(num-1)
        print(F"\n'{removed['title']}' deleted!")
    except (ValueError, IndexError):
        print("\nInvalid number.")

while True:
    show_menu()
    choice = input("\nChoose an option: ")
    if choice == '1': add_task()
    elif choice == '2': show_tasks()
    elif choice == '3': delete_task()
    elif choice == '4':
        print("\nBye!")
        break
    else:
        print("\nInvalid choice.")