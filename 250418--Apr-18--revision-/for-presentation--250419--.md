

=====================================================


=====================================================



## ✅ Python Modules Used and Their Functions**

---

###  `json` module  
The `json` module is used to **read from and write to JSON files**, and to **convert Python objects to JSON strings and vice versa**.

#### 🔹 `json.load()`
- Used to **read and parse** a JSON file and convert it to a Python object (usually a list or dictionary).
```python
json_loaded = json.load(json_file)
```

#### 🔹 `json.dump()`
- Used to **write a Python object to a JSON file**, serializing it as a JSON formatted string.
```python
json.dump(json_loaded, json_file)
```

#### 🔹 `json.dumps()`
- Converts a Python object to a **JSON formatted string**. Helpful for **pretty printing**.
```python
json_loaded_str = json.dumps(json_loaded, indent=2)
```

---

###  `datetime` module  
The `datetime` module is used to **work with dates and times**.

#### 🔹 `datetime.datetime.now()`
- Returns the **current date and time**.
```python
datetime.datetime.now()
```

#### 🔹 `strftime()`
- Formats a datetime object as a string using a **specified format**.
```python
datetime.datetime.now().strftime('%d/%m/%y, %H:%M:')
```

---

## ✅ Functions, Methods, and Data Structures Used**

---

###  `open()` function  
Used to **open files** in different modes (`'r'` for read, `'w'` for write).

```python
with open(json_filename, 'r') as json_file:
```

---

###  `with` statement  
Used for **context management**. Ensures files are **properly closed** after operations are done.

```python
with open(json_filename, 'w') as json_file:
```

---

###  `for` loop  
Used to **iterate over lists**, such as looping through all tasks.

```python
for iii in json_loaded:
```

---

###  `if` statement  
Used for **conditional checks**, e.g., checking if a task is completed.

```python
if task["is_completed"] == False:
```

---

###  `list` (Data Structure)  
A list is used to **store multiple task dictionaries**.

```python
json_loaded = json.load(json_file)  # json_loaded is a list
```

To store filtered tasks:
```python
tasks_pending = []
```

---

###  `dict` (Data Structure)  
Each task is stored as a **dictionary** containing keys like `"title"`, `"due_date"`, etc.

```python
task = {
  "title": "python",
  "due_date": "18/04/26, 16:03:",
  "priority": "low",
  "is_completed": False
}
```

---

###  `append()` method (for list)  
Used to **add a new task dictionary to the task list**.

```python
json_loaded.append(task)
```

---

###  `print()` function  
Used to **display output to the console**, for debugging and tracking.

```python
print(json_loaded_str)
```

---

###  `==` operator  
Used to **compare values**, such as checking if a task is completed.

```python
if task["is_completed"] == False:
```

---

Let me know if you’d like a visual diagram of how the components interact or a refactor into class-based style.

=====================================================


=====================================================