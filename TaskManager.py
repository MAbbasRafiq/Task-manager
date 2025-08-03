import os

FileName = "tasks.txt"

# Add tasks to dictionary
def add_task(tasks):
    title = input("Enter task title: ")
    task_id = max(tasks.keys(), default=0) + 1
    tasks[task_id] = {"title": title, "status": "Incomplete"}
    print(f"Task '{title}' added successfully")
    print(tasks)
    
# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks added")
    else:
        print("\nCurrent Tasks:")
        print(f"{'ID':<5} {'Title':<30} {'Status'}")
        print("-" * 50)
        
        for task_id, task in tasks.items():
            print(f"{task_id:<5} {task['title']:<30} {task['status']}")



# Mark task as completed
def mark_task_complete(tasks):
    try:
        taskid = int(input("Enter task id to mark it as completed: "))
        if taskid in tasks.keys():
            tasks[taskid]['status'] = "Completed"
            print(f"Task '{tasks[taskid]['title']}' marked complete")
            
        else:
            print(f"Task of id '{taskid}' not found.")
            
    except ValueError:
        print(f"Enter valid task id to mark it as completed.")

# Delete Task
def delete_task(tasks):
    try:
        taskid = int(input("Enter task id to delete: "))
        if taskid in tasks.keys():
            del tasks[taskid]
            print(f"Task deleted successfully")
            
        else:
            print(f"Task of id '{taskid}' not found.")
            
    except ValueError:
        print(f"Enter valid int task id to delete.")

# save_tasks to file from dictionary
def save_tasks(tasks):
    with open(FileName, "w") as file:
        for task_id, task in tasks.items():
            file.write(f"{task_id} | {task['title']} | {task['status']}\n")

# load tasks to dictionary
def load_tasks():
    tasks = {}
    
    if os.path.exists("tasks.txt"):
        with open(FileName, "r") as file:
            for line in file:
                task_id, title, status = line.strip().split(" | ")
                tasks[int(task_id)] = {"title": title, "status": status}
    return tasks

# Main Menu
def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid Choice. Please try again")


if __name__ == "__main__":
    main()