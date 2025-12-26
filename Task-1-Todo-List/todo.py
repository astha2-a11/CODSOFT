# Task1 To-Do List Program 

tasks = []  

while True:

    print("\n--- TO DO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")


    choice = input("Enter your choice: ")

  
    if choice == "1":
        task = input("Enter task name: ")
        tasks.append(task)
        print("Task added successfully!")

    
    elif choice == "2":
        if not tasks:
            print("No tasks available")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

   
    elif choice == "3":
        if not tasks:
            print("No tasks to update")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])
            num = int(input("Enter task number to update: "))
            tasks[num - 1] = input("Enter new task: ")
            print("Task updated successfully!")

    elif choice == "4":
        if not tasks:
            print("No tasks to delete")
        else:
            for i in range(len(tasks)):
                print(i + 1, tasks[i])
            num = int(input("Enter task number to delete: "))
            tasks.pop(num - 1)
            print("Task deleted successfully!")

    elif choice == "5":
        print("Thank you! Program ended 😊")
        break
    else:
        print("Invalid choice, try again")


