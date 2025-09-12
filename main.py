""" main.py """

import sys
from execute_command import execute_command

def main():
  arguments = sys.argv
  execute_command(arguments)

if __name__ == "__main__":
  main()