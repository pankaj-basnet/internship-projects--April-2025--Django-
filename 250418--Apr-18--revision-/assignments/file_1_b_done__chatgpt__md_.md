It looks like you're building a To-Do List Manager, where you're implementing various functionalities like adding tasks, marking tasks as completed, listing pending/completed tasks, and saving/loading the tasks using a `.json` file. You've already written some code to accomplish these tasks. I'll help you organize and improve it a little bit for clarity, and also give suggestions for improving certain parts.

### Here's a cleaned-up and structured version of the code:

```python
import datetime
import json

json_filename = 'data.json'

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
    new_task = add_task("Finish Assignment", "high")
    tasks.append(new_task)
    
    # Mark a task as completed
    tasks = mark_task_completed("18/04/26, 16:03:", tasks)
    
    # Save the updated task list
    save_tasks(tasks)
    
    # List all tasks
    list_tasks(tasks)
    
    # List pending tasks
    list_pending_tasks(tasks)

# Run the application
if __name__ == "__main__":
    main()
```

### Key Improvements & Features:
1. **Modular Functions**: Each task (loading, saving, adding, etc.) is now encapsulated in its own function, making the code more reusable and maintainable.
2. **File Handling**: The `load_tasks()` function gracefully handles the case when the JSON file does not exist (i.e., when starting with an empty task list).
3. **Task Addition**: The `add_task()` function simplifies task creation by accepting a title and priority. It automatically generates the current date and time.
4. **Marking Tasks as Completed**: The `mark_task_completed()` function updates the `is_completed` field for the task with the provided due date.
5. **Listing Pending Tasks**: The `list_pending_tasks()` function only lists tasks that are not completed.
6. **Error Handling**: The code checks if the task exists before trying to mark it as completed. If the task isn't found, it prints a message.

### Key Notes:
- **Appending to JSON files**: Generally, appending data directly to a JSON file can be problematic, especially if you don't want to overwrite or lose existing data. It's better to read, modify the list, and then write the entire list back to the file.
- **JSON Format**: In your original code, tasks are stored as dictionaries in a list. This is a good approach, as it makes it easy to manipulate individual tasks.
- **Task Search by Due Date**: When marking a task as completed, you're checking against a specific due date. This works well as long as you're consistent with the format (e.g., `dd/mm/yy, hh:mm:`).

---

Let me know if you'd like to add more features or need further clarification on any part!