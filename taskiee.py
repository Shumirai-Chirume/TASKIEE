# TASKIEE - A simple Task Manager for Students
tasks = []

def show_menu():
    print("\n=== TASKIEE MENU ===")
    print("1, Add a task")
    print("2. View tasks")
    print("3. Mark task as done") #new item
    print("4. Delete a task")
    print("5. Filter tasks by priority")
    print("6. Exit")

def add_task():
    task_name = input("Enter a task: ")

    priority = input("Enter priority (high / medium / low): ").lower() #new update

    if priority not in ["high", "medium", "low"]:
        print("INVALID priority. Task not added.")
        return

    task = {"name": task_name, "DONE!": False, "priority": priority} #new update
    tasks.append(task)
    print("TASK ADDED! with priority: ",priority)

def view_task():
    if not tasks:
        print("NO TASKS YET")
    else:
        print("\n Your Tasks: ")
        for i, task in enumerate(tasks, start=1):
            status = "DONE!" if task["DONE!"] else " " #checks if done
            print(f"{i}. [{status}] {task['name']} (Priority: {task['priority']})")

def mark_task_done():
    view_task()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to mark as done: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["DONE!"] = True
            print("Task Marked as Done!")
        else:
            print("INVALID task number.")
    except ValueError:
        print("Please enter a number.")

def delete_task():
    view_task()
    if not tasks:
        return
    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task['name']}' DELETED!")
        else:
            print("INVALID task number.")
    except ValueError:
        print("Please enter a valid number.")

def filter_tasks_by_priority():
    priority = input("Enter priority to filter by (high / medium / low): ").lower()

    if priority not in ["high", "medium", "low"]:
        print("INVALID priority!")
        return

    filtered_tasks = [task for task in tasks if task["priority"] == priority]
    if not filtered_tasks:
        print(f"No {priority} priority task(s) found.")
    else:
        print(f"\n {priority.lower()} priority task(s) found.")
    for i, task in enumerate(filtered_tasks, start=1):
        status = "DONE!" if task["DONE!"] else " "
        print(f"{i}. [{status}] {task['name']}")

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_task()
    elif choice == "3":
        mark_task_done()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        filter_tasks_by_priority()
    elif choice == "6":
        print("Goodbye from TASKIEE")
        break
    else:
        print("INVALID CHOICE TRY AGAIN!")