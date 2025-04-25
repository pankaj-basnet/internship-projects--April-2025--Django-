# Assignment - 1
# To-Do List Manager

# Features:

#     Add a task (title, due date, priority)

#     Mark task as completed

#     List pending/completed tasks

#     Store tasks in a .json or .csv file

#     Load tasks on app start

print("============================================")
import datetime
import json

json_filename = 'data__chatgpt_.json'

# Function to load tasks from the JSON file
def load_tasks():
    try:
        with open(json_filename, 'r') as json_file:
            print("Loading all tasks...")
            tasks = json.load(json_file)
            return tasks
    except FileNotFoundError:
        print("File not found. Starting with an empty task list.")
        return []

# Function to save tasks to the JSON file
def save_tasks(tasks):
    with open(json_filename, 'w') as json_file:
        json.dump(tasks, json_file, indent=2)
        print("Tasks saved to file.")

# Function to add a new task
def add_task(title, priority="low"):
    task = {
        "title": title,
        "due_date": datetime.datetime.now().strftime('%d/%m/%y, %H:%M:'),
        "priority": priority,
        "is_completed": False
    }
    return task

# Function to mark a task as completed
def mark_task_completed(due_date, tasks):
    for task in tasks:
        if task["due_date"] == due_date:
            task["is_completed"] = True
            print(f"Task marked as completed: {task}")
            return tasks
    print(f"No task found with due date {due_date}")
    return tasks

# Function to list all tasks
def list_tasks(tasks):
    print("Listing all tasks:")
    for task in tasks:
        print(f"Title: {task['title']}, Due Date: {task['due_date']}, Priority: {task['priority']}, Completed: {task['is_completed']}")

# Function to list pending tasks
def list_pending_tasks(tasks):
    pending_tasks = [task for task in tasks if not task["is_completed"]]
    print("Pending tasks:")
    for task in pending_tasks:
        print(f"Title: {task['title']}, Due Date: {task['due_date']}, Priority: {task['priority']}")
    return pending_tasks

# Main application logic
def main():
    tasks = load_tasks()
    
    # Add a new task
    new_task = add_task("grow assingment", "medium")
    tasks.append(new_task)
    
    print("-----------------------------------")
    # Mark a task as completed
    tasks = mark_task_completed("18/04/26, 16:03:", tasks)
    
    print("-----------------------------------")
    # Save the updated task list
    save_tasks(tasks)
    
    print("-----------------------------------")
    # List all tasks
    list_tasks(tasks)
    
    print("-----------------------------------")
    # List pending tasks
    list_pending_tasks(tasks)
    print("-----------------------------------")

# Run the application
if __name__ == "__main__":
    main()

print("============================================")
