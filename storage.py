""" storage.py """

import json
import os
import datetime

data_file = "tasks_data.json"

def ensure_data_file_initialized() -> None:
  if not os.path.exists(data_file) or os.stat(data_file).st_size == 0:
    with open(data_file, "w", encoding="utf-8") as f:
      json.dump([], f, indent=2)
      
def check_task_exists(description=None, id=None, by_desc=False, by_id=False) -> bool: 
  # Cheks if the task exists or not

  ensure_data_file_initialized()

  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)
    for task in tasks:
      if by_desc:
        if task.get("description") == description:
          return True
      if by_id:
          if task.get("id") == id:
            return True
    return False

def fetch_task_by_id(id: int) -> None:  
  # Used after checking task_existence, so ensuring data file initialization is not necessary

  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for task in tasks:
      if task.get("id") == int(id):
        return task
  return 

def save_new_task(description: str) -> None:

  ensure_data_file_initialized()
  
  with open(data_file, encoding="utf-8") as f: 
    
    tasks = json.load(f) 

    new_task = {
      "id": max((task["id"] for task in tasks), default=0) + 1,
      "description": description,
      "status": "todo",
      "createdAt": datetime.datetime.now().isoformat(),
      "updatedAt": datetime.datetime.now().isoformat()
    }

    with open(data_file, "w", encoding="utf-8") as f:
      tasks.append(new_task)
      json.dump(tasks, f, indent=2)

def modify_task(task, new_description) -> bool: 
  # Used after checking task_existence, so ensuring data file initialization is not necessary

  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for t in tasks:
      if t != task and t.get('description') == new_description:
        return False

    for t in tasks:
        if t == task:
          t["description"] = new_description
          t["updatedAt"] = datetime.datetime.now().isoformat()
          break

    with open(data_file, "w", encoding="utf-8") as f:
      json.dump(tasks, f, indent=2)
    return True
  
def remove_task(task) -> None:
  # Used after checking task_existence, so ensuring data file initialization is not necessary

  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)
    if task in tasks:
      tasks.remove(task)
      with open(data_file, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def set_task_in_progress(task) -> None:
  # Used after checking task_existence, so ensuring data file initialization is not necessary

  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for t in tasks:
      if t == task:
        t['status'] = 'in-progress'
        t['updatedAt'] = datetime.datetime.now().isoformat()
        break
    with open(data_file, "w", encoding="utf-8") as f:
      json.dump(tasks, f, indent=2)
    
def set_task_done(task) -> None:
  # Used after checking task_existence, so ensuring data file initialization is not necessary

  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    for t in tasks:
      if t == task:
        t['status'] = "done"
        t['updatedAt'] = datetime.datetime.now().isoformat()
        break
    
    with open(data_file, "w", encoding="utf-8") as f:
      json.dump(tasks, f, indent=2)
  
def get_every_task() -> list:

  ensure_data_file_initialized()

  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    return tasks
  
def get_done_tasks() -> list:

  ensure_data_file_initialized()

  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    return [task for task in tasks if task.get('status') == 'done']
    
def get_todo_tasks() -> list:

  ensure_data_file_initialized()
  
  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    return [task for task in tasks if task.get('status') == 'todo']    
  
def get_in_progress_tasks() -> list:

  ensure_data_file_initialized()
  
  with open(data_file, "r", encoding="utf-8") as f:
    tasks = json.load(f)

    return [task for task in tasks if task.get('status') == 'in-progress'] 