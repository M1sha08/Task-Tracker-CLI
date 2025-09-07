import json
import os
import datetime

tasks_data = "tasks_data.json"


def create_task(description):

  if not os.path.exists(tasks_data):
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
  
  with open(tasks_data, encoding="utf-8") as f:

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


