import json
import os
import datetime

tasks_data = "tasks_data.json"

def data_file_exists():
  if os.path.exists(tasks_data):
    return True
  return False

def create_task(description):

  if not data_file_exists(): # Create file and create first task if file doesn't exists
    with open(tasks_data, "w", encoding="utf-8") as f:

      task = {
        "id": 1,
        "description": description,
        "status": "todo",
        "createdAt": datetime.datetime.now().isoformat(),
        "updatedAt": datetime.datetime.now().isoformat()
      }

      json.dump([task], f, indent=2)
      return
  
  with open(tasks_data, encoding="utf-8") as f: # Add task to the data if file already exists
    
    tasks = json.load(f) 

    new_task = {
      "id": max(task["id"] for task in tasks) + 1,
      "description": description,
      "status": "todo",
      "createdAt": datetime.datetime.now().isoformat(),
      "updatedAt": datetime.datetime.now().isoformat()
    }

    with open(tasks_data, "w", encoding="utf-8") as f:
      tasks.append(new_task)
      json.dump(tasks, f, indent=2)

def task_exists(description):
  # Cheks if the task exists or not

  if not data_file_exists(): # Task automatically doesn't exists if there's no data at all
    return False

  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)
    for task in tasks:
      if task.get("description") == description:
        return True
    return False

def get_task_by_id(id):

  if not data_file_exists():
    return False
  
  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for task in tasks:
      if task.get("id") == id:
        return task
  return False

def update_task(task, new_description):

  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for t in tasks:
      if t["id"] == task["id"]:
        t["description"] = new_description
        t["updatedAt"] = datetime.datetime.now().isoformat()
        break

    with open(tasks_data, "w", encoding="utf-8") as f:
      json.dump(tasks, f, indent=2)
  
