import storage

def execute_command(arguments):

  commands = [
      {"command": "add", "action": add_task, "required_args": 1},
      {"command": "update", "action": update_task, "required_args": 2},
      {"command": "delete", "action": ..., "required_args": 1},
      {"command": "mark-in-progress", "action": ..., "required_args": 1},
      {"command": "mark-done", "action": ..., "required_args": 1},
      {"command": "list", "action": ..., "required_args": 0},
      {"command": "list-done", "action": ..., "required_args": 0},
      {"command": "list-todo", "action": ..., "required_args": 0},
      {"command": "list-in-progress","action": ..., "required_args": 0},
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
  
def add_task(description):
  if not storage.task_exists(description):
    storage.create_task(description)
  else:
    print("Task already exists, try updating it instead.")

def update_task(id, new_description):
  id = int(id)

  if task := storage.get_task_by_id(id):
    storage.update_task(task, new_description)
    print(f"Task with ID {id} updated successfully.")
  else:
    print(f"No task found with the ID {id}!")


def delete_task():
  ...

def mark_in_progress():
  ...

def mark_done():
  ...

def list_tasks():
  ...

def list_done_tasks():
  ...

def list_todo_tasks():
  ...

def list_in_progress_tasks():
  ...
  
def show_help():
  print("Help")
