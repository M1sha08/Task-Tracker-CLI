""" task_manager """

import storage
import utils

def handle_add_task(description: str) -> None:
  if not storage.check_task_exists(description, by_desc=True):
    storage.save_new_task(description)
    print("Task added successfully.")
  else:
    print("Task already exists, try updating it instead.")

def handle_update_task(id: int, new_description: str) -> None:

  if not utils.is_valid_int(id):
    print(f"Invalid ID: ({id}). It must be an integer.")
    return
  id = int(id)

  if storage.check_task_exists(id=id, by_id=True):
    task = storage.fetch_task_by_id(id)
    if storage.modify_task(task, new_description):
      print(f"Task with ID {id} was successfully updated.")
    else:
      print("Task with similar description exists.")
  else:
    print(f"No task found with the ID {id}!")

def handle_delete_task(id: int) -> None:

  if not utils.is_valid_int(id):
    print(f"Invalid ID: ({id}). It must be an integer.")
    return
  id = int(id)

  if storage.check_task_exists(id=id, by_id=True):
    task = storage.fetch_task_by_id(id)
    storage.remove_task(task)
    print(f"Task with ID {id} was successfully deleted.")
  else:
    print(f"Couldn't find the task with ID {id}.")

def handle_mark_in_progress(id: int) -> None:

  if not utils.is_valid_int(id):
    print(f"Invalid ID: ({id}). It must be an integer.")
    return
  id = int(id)

  if storage.check_task_exists(id=id, by_id=True):
    task = storage.fetch_task_by_id(id)
    storage.set_task_in_progress(task)
  else:
    print(f"Couldn't find the task with ID {id}.")

def handle_mark_done(id: int) -> None:

  if not utils.is_valid_int(id):
    print(f"Invalid ID: ({id}). It must be an integer.")
    return
  id = int(id)

  if storage.check_task_exists(id=id, by_id=True):
    task = storage.fetch_task_by_id(id)
    storage.set_task_done(task)
  else:
    print(f"Couldn't find the task with ID {id}.")

def handle_list_tasks() -> None:

  tasks = storage.get_every_task()

  if not tasks:
    print("No tasks to show.")
    return

  utils.list_tasks(tasks)

def handle_list_done_tasks() -> None:
  done_tasks = storage.get_done_tasks()

  if not done_tasks:
    print("No tasks with status 'done' to show.")
    return
  
  utils.list_tasks(done_tasks)
  
def handle_list_todo_tasks() -> None:
  todo_tasks = storage.get_todo_tasks()

  if not todo_tasks:
    print("No tasks with status 'todo' to show.")
    return

  utils.list_tasks(todo_tasks)

def handle_list_in_progress_tasks() -> None:
  in_progress_tasks = storage.get_in_progress_tasks()

  if not in_progress_tasks:
    print("No tasks with status 'in-progress' to show.")
    return
  
  utils.list_tasks(in_progress_tasks)