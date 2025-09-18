# Day 14 - To-Do List App (with tasks saved to a text file)

TASKS_FILE = "tasks.txt"

# --- Helper Functions ---
def load_tasks():
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return [] 


def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(task + "\n")


tasks = load_tasks()

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
        save_tasks(tasks)
        print(f"Added task: {task}")

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            print("\nYour tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            try:
                num = int(input("Enter the number of the task to remove: "))
                removed = tasks.pop(num - 1)
                save_tasks(tasks)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid choice.")

    elif choice == "4":
        save_tasks(tasks)  
        print("Goodbye!")
        break

    else:
        print("Please choose a valid option (1-4).")
