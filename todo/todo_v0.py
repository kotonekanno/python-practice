tasks = []
def show_menu():
    print("\n====  ToDo Menu ====")
    print("1: Add Task")
    print("2: Show Tasks")
    print("3: Delete Task")
    print("4: Exit")

def add_task():
    task = input("\nEnter a task: ")
    tasks.append(task)
    print(f"\n'{task}' added!")

def show_tasks():
    if not tasks:
        print("\nno tasks.")
    else:
        print("\nTasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}.{task}")

def delete_task():
    show_tasks()
    try:
        num = int(input("\nEnter task number: "))
        removed = tasks.pop(num-1)
        print(F"\n'{removed}' deleted!")
    except (ValueError, IndexError):
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
