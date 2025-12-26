# task1---To Do list
tasks = []

def show_menu():
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Task")
    print("3. Complete Task")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task Added")

def view_task():
    if not tasks:
        print("No tasks")
    else:
        for i in range(len(tasks)):
            print(i + 1, tasks[i])

def complete_task():
    view_task()
    n = int(input("Task number completed: "))
    print("Task Completed:", tasks[n-1])

def update_task():
    view_task()
    n = int(input("Task number to update: "))
    tasks[n-1] = input("New task: ")

def delete_task():
    view_task()
    n = int(input("Task number to delete: "))
    tasks.pop(n-1)

while True:
    show_menu()
    ch = input("Enter choice: ")

    if ch == "1":
        add_task()
    elif ch == "2":
        view_task()
    elif ch == "3":
        complete_task()
    elif ch == "4":
        update_task()
    elif ch == "5":
        delete_task()
    elif ch == "6":
        print("Thank You 😊")
        break
    else:
        print("Wrong choice")
