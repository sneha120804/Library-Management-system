# 📚 Library Management System

A simple and user-friendly **Library Management System** built using **Python and Tkinter**.

This project helps manage books in a library by allowing users to **view available books, borrow books, return books, search for books, and track the total number of available books** through a modern desktop interface.

---

## 🖥️ Project Preview

> A modern dark-themed library dashboard designed using Python Tkinter.

**Main Features:**

* 📚 View available books
* 📤 Borrow books
* 📥 Return books
* 🔍 Search books
* 📊 View total available books
* 🕒 Display borrowing date and time
* 🎨 Modern dashboard-style GUI
* ❌ Easy exit option

---

## ✨ Features

### 📖 View Available Books

Displays all books currently available in the library with their serial numbers.

### 📤 Borrow a Book

Users can enter their name and the name of the book they want to borrow.

If the book is available:

* The book is removed from the available-books list.
* The user's name is displayed.
* The borrowing date and time are recorded.

### 📥 Return a Book

Users can return a previously borrowed book by entering its name.

The book is added back to the library collection.

### 🔍 Search a Book

Search for a particular book using its name.

The system displays whether the book is currently available.

### 📊 Total Books

The dashboard automatically displays the current number of available books.

### 🎨 Graphical User Interface

The project uses **Tkinter** to provide a simple desktop GUI with:

* Sidebar navigation
* Dashboard
* Statistics cards
* Search bar
* Book collection panel
* Quick action buttons
* Dark-themed interface

---

## 🛠️ Technologies Used

| Technology  | Purpose                           |
| ----------- | --------------------------------- |
| 🐍 Python   | Main programming language         |
| 🖼️ Tkinter | Graphical User Interface          |
| 🕒 datetime | Borrowing date and time           |
| 🧱 OOP      | Library class and book management |

---

## 🧠 Python Concepts Used

This project demonstrates several important Python concepts:

* Classes and Objects
* `__init__()` constructor
* Instance variables
* Methods
* Lists
* `for` loops
* Conditional statements
* Functions
* String methods
* `enumerate()`
* `len()`
* `datetime`
* Tkinter GUI
* Event-driven programming
* Basic exception/input validation

---

## 📂 Project Structure

```text
Library-Management-System/
│
├── library_management.py
│
├── screenshots/
│   ├── dashboard.png
│   ├── borrow.png
│   ├── return.png
│   └── search.png
│
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Library-Management-System.git
```

### 2. Open the Project

```bash
cd Library-Management-System
```

### 3. Run the Python File

```bash
python library_management.py
```

The Library Management System GUI will open.

---

## 📚 Books Included

The project currently contains books related to programming, computer science, artificial intelligence, databases, and software engineering.

Some examples include:

* Python Crash Course
* Clean Code
* Introduction to Algorithms
* Head First Java
* Data Structures and Algorithms
* The Pragmatic Programmer
* Computer Networks
* Operating System Concepts
* Database System Concepts
* Artificial Intelligence: A Modern Approach
* Machine Learning
* Deep Learning
* Learning SQL
* Django for Beginners
* Flask Web Development
* Software Engineering
* The C Programming Language

---

## 🔄 How the System Works

```text
                    ┌────────────────────┐
                    │       START        │
                    └─────────┬──────────┘
                              │
                              ▼
                  ┌──────────────────────┐
                  │  Library Dashboard   │
                  └──────────┬───────────┘
                             │
             ┌───────────────┼───────────────┐
             │               │               │
             ▼               ▼               ▼
        📖 View Books    📤 Borrow       📥 Return
             │               │               │
             │               ▼               │
             │        Check Availability     │
             │               │               │
             │        ┌──────┴──────┐        │
             │        │             │        │
             │       YES            NO       │
             │        │             │        │
             │        ▼             ▼        │
             │     Remove        Show Error  │
             │      Book                      │
             │                                │
             │               ◄────────────────┘
             │
             ▼
        🔍 Search Book
             │
             ▼
       Display Result
             │
             ▼
            EXIT
```

---

## 💡 Future Improvements

The current project uses a Python list to store books. Future versions can include:

* 🗄️ SQLite/MySQL database integration
* 👤 User login and registration
* 🔐 Admin login
* 📅 Book due dates
* 💰 Fine calculation
* 📜 Borrowing history
* 🏷️ Book categories
* 👨‍💼 Member management
* 📊 Library statistics
* 📱 Responsive web version
* ☁️ Cloud database integration

---

## 🎯 Project Objective

The main objective of this project is to develop a simple library management application while applying **Python programming, Object-Oriented Programming, data handling, and GUI development concepts**.


