tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. Show Tasks")
    print("3. Remove Task")
    print("4. Quit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print(f"Added task {task}")
    
    elif choice == "2":
        if not tasks:
            print("No tasks in the list")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove")
        else:
            for i, task in enumerate(tasks,start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter the number of the task you wish to remove: "))
                removed = tasks.pop(num - 1)
                print(f"Removed: {removed}")
            except(ValueError,IndexError):
                print("invalid choice")

    elif choice == "4":
        print("Goodbye")
        break
    else:
        print("Please choose a valid option (1-4)")