""" utils.py """

def is_valid_int(value) -> bool:
  try:
    int(value)
    return True
  except ValueError:
    return False
  
def list_tasks(tasks: list[dict]) -> None:

  ID_SPACE = 8
  STATUS_SPACE = 15
                    
  print(f"\n{'Task ID':<{ID_SPACE}} | {'Task Status':<{STATUS_SPACE}} | Task Description")
  print("-"*55)

  for task in tasks:
    print(f"{task.get('id'):<{ID_SPACE}} | {task.get('status'):<{STATUS_SPACE}} | {task.get('description')}")