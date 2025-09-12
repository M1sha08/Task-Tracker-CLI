""" execute_command.py """

import task_manager

def execute_command(arguments):
  commands = [
    {"cmd": "add", "action": task_manager.handle_add_task, "required_args": 1, "example": "[<add> <description>]"},
    {"cmd": "update", "action": task_manager.handle_update_task, "required_args": 2, "example": "[<update> <task id> <new description>]"},
    {"cmd": "delete", "action": task_manager.handle_delete_task, "required_args": 1, "example": "[<delete> <task id>]"},
    {"cmd": "mark-in-progress", "action": task_manager.handle_mark_in_progress, "required_args": 1, "example": "[<mark-in-progress> <task id>]"},
    {"cmd": "mark-done", "action": task_manager.handle_mark_done, "required_args": 1, "example": "[<mark-done> <task id>]"},
    {"cmd": "list", "action": task_manager.handle_list_tasks, "required_args": 0, "example": "[<list>]"},
    {"cmd": "list-done", "action": task_manager.handle_list_done_tasks, "required_args": 0, "example": "[<list-done>]"},
    {"cmd": "list-todo", "action": task_manager.handle_list_todo_tasks, "required_args": 0, "example": "[<list-todo>]"},
    {"cmd": "list-in-progress", "action": task_manager.handle_list_in_progress_tasks, "required_args": 0, "example": "[<list-in-progress>]"},
    {"cmd": "show-info", "action": show_info, "required_args": 0, "example": "[<show-info>]"},
  ]

  
  if len(arguments) > 1:
    for command in commands:
      if arguments[1] == command.get('cmd'):
        if len(arguments) - 2 == command.get('required_args'):
          command['action'](*arguments[2:])
          break
        else:
          print(f"Command '{command.get('cmd')}' takes {command.get('required_args')} argument(s), but you gave {len(arguments) - 2}.")
          print(f"Example: {command.get('example')}")
          break
    else:
      print("Unknown command. Use 'show-info' command for more information.")
  else:
    print("No command provided. Try 'show-info' for guidance.")

def show_info() -> None:
    print("Information about this program".center(70, "_"))
    print("\nThis is a basic CLI Task Tracker program. Made by GitHub: M1sha08\n")
    print(f"{'Command':<25} | {'Description':<35} | Example")
    print("-"*80)
    
    commands = [
        ("add", "Add task", "<add> <description>"),
        ("update", "Update task", "<update> <task id> <new description>"),
        ("delete", "Delete task", "<delete> <task id>"),
        ("mark-in-progress", "Mark task as in progress", "<mark-in-progress> <task id>"),
        ("mark-done", "Mark task as done", "<mark-done> <task id>"),
        ("list", "Show all tasks", "<list>"),
        ("list-done", "Show tasks with status done", "<list-done>"),
        ("list-todo", "Show tasks with status todo", "<list-todo>"),
        ("list-in-progress", "Show tasks with status in-progress", "<list-in-progress>"),
        ("show-info", "Show program information", "<show-info>")
    ]
    
    for cmd, desc, example in commands:
        print(f"{cmd:<25} | {desc:<35} | {example}")