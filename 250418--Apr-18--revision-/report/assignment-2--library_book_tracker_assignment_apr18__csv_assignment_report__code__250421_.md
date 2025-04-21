
# 📘 Assignment - 2: Library Book Tracker

## 🧩 Features Implemented:
- Add a book (title, author, genre, borrowed date)
- Mark book as returned
- List currently borrowed books
- Show overdue books (based on borrow date)
- Store in `.csv` file

---

## ✅ Code Review

### 🔍 Problems faced:
1. **Boolean values as strings:** `'True'` and `'False'` from CSV are strings, not booleans. This leads to logical bugs.
2. **Redundant field headers:** Re-defining `fieldnames` while reading CSV could be risky, especially if the file format evolves.
3. **Header duplication:** `writeheader()` is not used consistently in append mode, which may cause repeated headers or misalignment.
4. **Hardcoded timestamp matching:** Using a fixed string timestamp to identify a row for updating is fragile. Use unique identifiers or date parsing.
5. **CSV reading assumptions:** Relying on `DictReader` with redefined fieldnames while skipping header rows can lead to misalignment.
6.  **Code structure:** Mixing reading, writing, and display logic in a single block reduces maintainability.

### 💡 lesson learned ( future notes for handling CSV ):
- Use `book['borrowed date'].isoformat()` when writing to CSV to ensure consistent formatting.
- Convert `'True'`/`'False'` using `value.lower() == 'true'` .
- When reading data, use `csv.Sniffer().has_header()` to handle potential double headers.
- Use functions to modularize: `add_book()`, `mark_returned()`, `list_borrowed()`, `show_overdue()`.

---

## 📊 (2) Assignment Summary Report

### 📌 Data Storage
- Stored in `file2.csv` using `csv.DictWriter()`.
- Headers: `title`, `author`, `genre`, `borrowed date`, `returned`.

### 📘 Sample Book Entry
```python
{
    "title": "Sherlock",
    "author": "many authors",
    "genre": "fantasy",
    "borrowed date": "2025-04-20T13:45:30",
    "returned": False
}
```

### 🔄 Marking Book as Returned
- Reads entire CSV into memory.
- Updates matching `borrowed date[:16]`.
- Writes updated rows back into the same file.

### 📋 Borrowed Books
- Filters rows where `"returned" == 'False'`.
- Prints titles with borrowed date.

### ⌛ Overdue Books
- Parses `borrowed date`.
- Adds 7 days and compares with current date.
- Prints due date per book.

---

## 🧠 Extra Note 

https://stackoverflow.com/questions/67496154/all-values-converted-to-strings-when-reading-csv

When handling boolean values in CSV files, always remember that CSV stores everything as strings. This causes unexpected behavior in logical checks like `if not value`, since `"False"` is still a non-empty string. It is best to explicitly cast the values using `value.strip().lower() == "true"` .

---

## 🧾 Additional Notes 

Handling `datetime` values in CSV files is tricky because CSV is a plain text format. Python’s `datetime` objects should be converted to strings using .strftime(format="%Y/%m/%d") method.
 
Avoid hardcoded timestamp checks (`[:16]`) — they’re brittle and prone to failure. 

Also, to maintain structure, modularize your code using functions. Keeping functions small and focused improves reusability and debugging.

---


---
---
---


```
                
          # Assignment - 2
          # Library Book Tracker

          # Features:
          #     Add a book (title, author, genre, borrowed date)
          #     Mark book as returned
          #     List currently borrowed books
          #     Show overdue books (based on borrow date)
          #     Store in .csv file

```

---
---
---