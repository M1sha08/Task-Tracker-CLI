""" storage.py """

import json
import os
import datetime

tasks_data = "tasks_data.json"

def check_data_file_exists() -> bool:
  if os.path.exists(tasks_data):
    return True
  return False

def check_task_exists(description=None, id=None, by_desc=False, by_id=False) -> bool: 
  # Cheks if the task exists or not

  if not check_data_file_exists(): # Task automatically doesn't exists if there's no data at all
    return False


  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)
    for task in tasks:
      if by_desc:
        if task.get("description") == description:
          return True
      if by_id:
        if id is not None:
          try:
            id_int = int(id)
          except (TypeError, ValueError):
            continue
          if task.get("id") == id_int:
            return True
    return False

def fetch_task_by_id(id) -> bool:
  
  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for task in tasks:
      if task.get("id") == int(id):
        return task
  return False

def save_new_task(description):

  if not check_data_file_exists() or os.stat(tasks_data).st_size < 5:
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

def modify_task(task, new_description):

  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for t in tasks:
      if t["id"] == task["id"]:
        t["description"] = new_description
        t["updatedAt"] = datetime.datetime.now().isoformat()
        break

    with open(tasks_data, "w", encoding="utf-8") as f:
      json.dump(tasks, f, indent=2)
  
def remove_task(task) -> bool:

  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)
    if task in tasks:
      tasks.remove(task)
      with open(tasks_data, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)
      return True

  return False

def set_task_in_progress(task):
  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for t in tasks:
      if t == task:
        t['status'] = 'in-progress'
        t['updatedAt'] = datetime.datetime.now().isoformat()
        break
    with open(tasks_data, "w", encoding="utf-8") as f:
      json.dump(tasks, f, indent=2)
    
def set_task_done(task):
  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for t in tasks:
      if t == task:
        t['status'] = "done"
        t['updatedAt'] = datetime.datetime.now().isoformat()
        break
    
    with open(tasks_data, "w", encoding="utf-8") as f:
      json.dump(tasks, f, indent=2)
  
def list_tasks_from_file() -> str:

  if not check_data_file_exists:
    return "No tasks yet!"

  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    if not tasks:
      return "No tasks yet!"

    tasks_list = "".join(
      f"\nID {task.get('id')} - Status: '{task.get('status')}': {task.get('description')}" for task in tasks)
    return tasks_list

def list_done_tasks_from_file() -> str:

  if not check_data_file_exists:
    return "No tasks yet!"

  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    done_tasks = [task for task in tasks if task.get('status') == 'done']
    if not done_tasks:
      return "No done tasks yet!"
    
    return "".join(
      f"\nID {task.get('id')} - Status: '{task.get('status')}': {task.get('description')}" for task in done_tasks
    )

def list_todo_tasks_from_file() -> str:

  if not check_data_file_exists():
    return "No tasks yet"
  
  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    todo_tasks = [task for task in tasks if task.get('status') == 'todo']

    if not todo_tasks:
      return "No tasks with status 'todo'!"
    
    return "".join(
      f"\nID: {task.get('id')} - Status: '{task.get('status')}': {task.get('description')}" for task in todo_tasks
    )
  
def list_in_progress_tasks_from_file() -> str:

  if not check_data_file_exists():
    return "No tasks yet"
  
  with open(tasks_data, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    in_progress_tasks = [task for task in tasks if task.get('status') == 'in-progress']

    if not in_progress_tasks:
      return "No tasks with status 'in-progress'!"
    
    return "".join(
      f"\nID {task.get('id')} - Status: '{task.get('status')}': {task.get('description')}" for task in in_progress_tasks
    )
    
