#締め切りと優先順位を追加できる
#編集できる

tasks = []
priorities = {
    1: "Very High",
    2: "High",
    3: "Medium",
    4: "Low",
    5: "Very Low"
}
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
    print("\n999 to Cancel")
    task["title"] = input("Enter a task: ")
    
    if task["title"] == '999': print()
    
    else:
        task['deadline'] = set_deadline()
        task['priority'] = prioritize()
        
        tasks.append(task)
        print(f"\n'{task['title']}' added!")
        print(f"The deadline is {task['deadline']}!")
        print(f"The priority is '{task['priority']}'!")

def set_deadline():
    try:
        deadline_pre = input("\nEnter the deadline (YYYY-MM-DD): ")
        deadline = datetime.strptime(deadline_pre,"%Y-%m-%d").date()
        return deadline
    
    except ValueError:
        print("\nInvalid number.")
        return set_deadline()

def prioritize():
    print("\n1. Very High")
    print("2. High")
    print("3. Medium")
    print("4. Low")
    print("5. Very Low")
    num_p = input("Choose the priority: ")
    
    if num_p in priorities.keys():
        priority = priorities[num_p]
        return priority
    
    else:
        print("\nInvalid number.")
        return prioritize()

def show_tasks():
    enumerate_tasks()

    print("\n--- Menu ---")
    print("1. Sort tasks")
    print("2. Exit")
    choice = input("Choose an option: ")

    if choice == '1': sort()
    elif choice == '2': return
    else:
        print("\nInvalid number.")
        return show_tasks()

def enumerate_tasks():
    if not tasks: print("\nNo tasks.")

    else:
        print("\nTasks:")
        today = datetime.now().date()

        for i, task in enumerate(tasks,1):
            print(f"{i}.{task['title']}  {task['deadline']}")

            time_left = task["deadline"] - today
            if task["deadline"] < today: print("     Expired!")
            else: print("    ",time_left.days,"days left!")
            
            print(f"     priority: {task['priority']}")

def sort():
    print("\n1. Sort by date")
    print("2. Sort by priority")
    print("3. Cancel")
    choice = input("Choose an option: ")
    
    if choice == '1':
        tasks.sort(key=lambda x: x["deadline"])
        return show_tasks()
    
    elif choice == '2':
        tasks.sort(key=lambda x: x["priority"])
        return show_tasks()
    
    elif choice == '3': show_tasks()
    
    else:
        print("\nInvalid number.")
        return sort()

def edit_task():
    while True:     #Choose a task to edit
        enumerate_tasks()
        print("\n999. Exit")
        try:
            num_e = int(input("Enter task number: "))
            if num_e == 999:
                print()
                return
            else: task = tasks[num_e-1]
        except (ValueError,IndexError):
            print("\nInvalid number.")
            continue

        while True:     #Choose an edit option
            print(F"\n{tasks[num_e-1]['title']}  {tasks[num_e-1]['deadline']}")
            print("\n1. Edit title")
            print("2. Reset deadline")
            print("3. Change priority")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':   #Edit title
                task['title'] = input("\nEnter a task: ")
                print(F"\nUpdated to '{tasks[num_e-1]['title']}'!")
            
            elif choice == '2':     #Reset deadline
                task['deadline'] = set_deadline()
                print(f"\nUpdated to {tasks[num_e-1]['deadline']}!")
            
            elif choice == '3':     #Reprioritize
                task['priority'] = prioritize()
                print(f"Updated to '{task['priority']}'!")
            
            elif choice == '4':
                break
                
            else:
                print("\nInvalid number.")
                continue

def delete_task():
    enumerate_tasks()

    try:
        print("\n999 to cancel")
        num_d = int(input("Enter task number: "))

        if num_d == 999: print()
        else:
            removed = tasks.pop(num_d-1)
            print(F"\n'{removed['title']}' deleted!")
    
    except(ValueError, IndexError):
        print("\nInvalid number.")
        return

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == '1': add_task()
    elif choice == '2': show_tasks()
    elif choice == '3': edit_task()
    elif choice == '4': delete_task()
    elif choice == '5':
        print("\nBye!")
        break
    
    else:
        print("\nInvalid choice.")