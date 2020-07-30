# Used to check if variables is defined appropriately
import decouple
from decouple import Csv


def env_check():
    try:
        repo_url = decouple.config('repo_url')
    except decouple.UndefinedValueError as repo_url_error:
        print("\nVariable 'repo_url' not defined in .env file")
        print("\nPlease ensure to define the 'repo_url' variable")
        exit(1)
    try:
        repo_path = decouple.config('repo_path')
    except decouple.UndefinedValueError as repo_path_error:
        print("\nVariable 'repo_path' not defined in .env file")
        print("\nPlease ensure to define the 'repo_path' variable")
        exit(1)
    try:
        uname = decouple.config('username')
    except decouple.UndefinedValueError as username_error:
        print("\nVariable 'username' not defined in .env file")
        print("\nPlease ensure to define the 'username' variable")
        exit(1)
    try:
          patterns = decouple.config('patterns')
    except decouple.UndefinedValueError as patterns_error:
        print("\nVariable 'patterns' not defined in .env file")
        print("\nPlease ensure to define the 'patterns' variable")
        exit(1)


env_check()
