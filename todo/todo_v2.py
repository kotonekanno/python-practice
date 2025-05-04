#優先順位を設定できる

tasks = []
def show_menu():
    print("\n====  ToDo Menu ====")
    print("1: Add Task")
    print("2: Show Tasks")
    print("3: Delete Task")
    print("4: Exit")

def add_task():
    task = {}
    task["title"] = input("\nEnter a task: ")
    print("\n1. Very High")
    print("2. High")
    print("3. Medium")
    print("4. Low")
    print("5. Very Low")
    task["priority"] = int(input("Choose the priority: "))
    tasks.append(task)
    print(f"\n'{task['title']}' added!")

def prioritize():
    tasks.sort(key=lambda x: x["priority"])

def show_tasks():
    prioritize()
    if not tasks:
        print("\nno tasks.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks,1):
            print(f"{i}.{task['title']}")

def delete_task():
    prioritize()
    show_tasks()
    try:
        num = int(input("\nEnter task number: "))
        removed = tasks.pop(num-1)
        print(F"\n'{removed['title']}' deleted!")
    except (ValueError,IndexError):
        print("\nInvalid number.")

while True:
    show_menu()
    choice = input("Choose an option: ")
    if choice == '1': add_task()
    elif choice == '2': show_tasks()
    elif choice == '3': delete_task()
    elif choice == '4':
        print("\nBye!")
        break
    else:
        print("\nInvalid choice.")