""" task_manager """

import storage

def execute_command(arguments):

  commands = [
      {"command": "add", "action": handle_add_task, "required_args": 1},
      {"command": "update", "action": handle_update_task, "required_args": 2},
      {"command": "delete", "action": handle_delete_task, "required_args": 1},
      {"command": "mark-in-progress", "action": handle_mark_in_progress, "required_args": 1},
      {"command": "mark-done", "action": handle_mark_done, "required_args": 1},
      {"command": "list", "action": handle_list_tasks, "required_args": 0},
      {"command": "list-done", "action": handle_list_done_tasks, "required_args": 0},
      {"command": "list-todo", "action": handle_list_todo_tasks, "required_args": 0},
      {"command": "list-in-progress","action": handle_list_in_progress_tasks, "required_args": 0},
      {"command": "help", "action": show_help, "required_args": 0}
    ]
  
  cmd_found = None
  if 1 < len(arguments) < 5:

    for cmd in commands:
      if arguments[1] == cmd["command"]:
        cmd_found = cmd
        break

    if cmd_found == None:
      print(f"Couldn't find command: '{arguments[1]}'")
      return
    
    if len(arguments) - 2 == cmd_found["required_args"]:
      cmd_found["action"](*arguments[2:])
      return
    print(f"The command '{cmd_found['command']}' expects {cmd_found['required_args']} argument(s), but you gave {len(arguments) - 2}") 

  else:
    print("Invalid amount of arguments! Enter 'help' for more information.")
    return
  
def handle_add_task(description):
  if not storage.check_task_exists(description, by_desc=True):
    storage.save_new_task(description)
  else:
    print("Task already exists, try updating it instead.")

def handle_update_task(id, new_description):
  id = int(id)

  if task := storage.fetch_task_by_id(id):
    storage.modify_task(task, new_description)
    print(f"Task with ID {id} updated successfully.")
  else:
    print(f"No task found with the ID {id}!")

def handle_delete_task(id):
  if storage.check_task_exists(id=id, by_id=True):
    task = storage.fetch_task_by_id(id)
    if not storage.remove_task(task):
      print("Error: Couldn't delete the task.")
      return
    print(f"Task with ID {id} was successfully deleted.")
  else:
    print(f"Error: Couldn't find the task with ID {id}.")

def handle_mark_in_progress(id):
  if storage.check_task_exists(id=id, by_id=True):
    task = storage.fetch_task_by_id(id)
    storage.set_task_in_progress(task)
  else:
    print(f"Error: Couldn't find the task with ID {id}.")

def handle_mark_done(id):
  if storage.check_task_exists(id=id, by_id=True):
    task = storage.fetch_task_by_id(id)
    storage.set_task_done(task)
  else:
    print(f"Error: Couldn't find the task with ID {id}.")

def handle_list_tasks():
  print(storage.list_tasks_from_file())

def handle_list_done_tasks():
  print(storage.list_done_tasks_from_file())
  
def handle_list_todo_tasks():
  print(storage.list_todo_tasks_from_file())

def handle_list_in_progress_tasks():
  print(storage.list_in_progress_tasks_from_file())
  
def show_help():
  print("Help")
