# Task Tracker (CLI)

### **A basic task tracking program** that accepts user actions and inputs as arguments, and stores tasks in a **JSON file**.

### This project was made with the goal to **learn more** (project idea from (https://roadmap.sh/projects/task-tracker)).

### **No external libraries** were used.

---

### **Instalation**

Clone the repository:

```bash
git clone https://github.com/M1sha08/Task-Tracker-CLI-.git
```

---

### **Structure**

```
Task Tracker (CLI)
|
|-- main.py - **entry point** hands arguments provided by user to execute_command.py
|--- execute_command.py - **parses commands** and calls a function from task_manager.py
|--- task_manager.py - **task-related logic** uses storage.py for data
|--- storage.py - **data-related functions**
|--- utils.py - **helper functions**
```

---

### **Features**

- **Add, Update, and Delete tasks**
- **Mark task** as _in progress_ or _done_
- **List all tasks**
- **List tasks separately** by status (`todo`, `in-progress`, `done`)

---

### **Task Properties**

- **`id`**: Unique identifier for the task
- **`description`**: Task description
- **`status`**: One of (`todo`, `in-progress`, `done`)
- **`createdAt`**: Date when task was created
- **`updatedAt`**: Date when task was last updated

---

### **How to Use**

Run this in your terminal: `python main.py <command> <arguments>`

| Command          | Description             | Example                                          |
| ---------------- | ----------------------- | -------------------------------------------------|
| add              | Add a new task          | `python main.py add 'id' "description"`          |
| update           | Update task description | `python main.py update 'id' "new description"`   |
| delete           | Delete a task           | `python main.py delete 'id'`                     |
| mark-in-progress | Mark task in-progress   | `python main.py mark-in-progress 'id'`           |
| mark-done        | Mark task as done       | `python main.py mark-done 'id'`                  |
| list             | List all tasks          | `python main.py list`                            |
| list-done        | List done tasks         | `python main.py list-done`                       |
| list-todo        | List todo tasks         | `python main.py list-todo`                       |
| list-in-progress | List in-progress tasks  | `python main.py list-in-progress`                |
| show-info        | Show program info       | `python main.py show-info`                       |
