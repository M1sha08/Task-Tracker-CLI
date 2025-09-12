""" main.py """

import sys, task_manager

def main():
  arguments = sys.argv
  task_manager.execute_command(arguments)

if __name__ == "__main__":
  main()
