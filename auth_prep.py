import decouple
import re
from urllib.parse import urlparse
from subprocess import Popen, PIPE
from OptionSelector import switch_check
import OptionSelector


# Used to check if variables is defined appropriately
def variable_check():

    print("######################################")
    print("Checking Environment Variables Defined")
    print("######################################")
    # Setting Variables as Global

    global repo_path
    global full_repo_url
    global patterns
    global folder

    try:
        repo_url = decouple.config('repo_url')
        if len(repo_url) <= 0:
            print("\u274c  'repo_url' is empty! Please ensure variable is defined correctly")
            exit(1)
        print(u'\u2714 "repo_url" variable is defined')
    except decouple.UndefinedValueError as repo_url_error:
        print("\n\u274c  Variable 'repo_url' not defined in .env file")
        print("\nPlease ensure to define the 'repo_url' variable")
        exit(1)
    try:
        repo_path = decouple.config('repo_path')
        if len(repo_path) <= 0:
            print("\u274c  'repo_path' is empty! Please ensure variable is defined correctly")
            exit(1)
        print(u'\u2714 "repo_path" variable is defined')
    except decouple.UndefinedValueError as repo_path_error:
        print("\n\u274c  Variable 'repo_path' not defined in .env file")
        print("\nPlease ensure to define the 'repo_path' variable")
        exit(1)

    try:
        if repo_url.startswith(("http://", "https://"), 0):
            try:
                uname = decouple.config('username')
                if len(uname) <= 0:
                    print("\u274c  'username' is empty! Please ensure variable is defined correctly")
                    exit(1)
                print(u'\u2714 "username" variable is defined')
            except decouple.UndefinedValueError as username_error:
                print("\n\u274c  Variable 'username' not defined in .env file")
                print("\nPlease ensure to define the 'username' variable")
                exit(1)
            try:
                pwd = decouple.config('app_password')
                if len(pwd) <= 0:
                    print("\u274c  'app_password' is empty! Please ensure variable is defined correctly")
                    exit(1)
                print(u'\u2714 "app_password" variable is defined')
            except decouple.UndefinedValueError as app_password_error:
                print("\n\u274c  Variable 'app_password' not defined in .env file")
                print("\nPlease ensure to define the 'app_password' variable")
                exit(1)

            parsed_url = urlparse(repo_url)
            creds = uname + ":" + pwd
            full_repo_url = f'{parsed_url.scheme}://{creds}@{parsed_url.netloc}{parsed_url.path}'
            # If above statement is false, assume the 'repo_url' as SSH URL
        else:
            full_repo_url = repo_url
    except:
        exit(1)

    if OptionSelector.options.__dict__['folder']:  # If true then >
        try:
            folder = decouple.config('folder')
            if len(folder) <= 0:
                print("\u274c  'folder' is empty! Please ensure variable is defined correctly")
                exit(1)
            print(u'\u2714 "folder" variable is defined')
        except decouple.UndefinedValueError as folder_error:
            print("\n\u274c  Variable 'folder' not defined in .env file")
            print("\nPlease ensure to define the 'folder' variable")
            exit(1)

    if OptionSelector.options.__dict__['patterns']:  # If true then >
        try:
            patterns = decouple.config('patterns')
            if len(patterns) <= 0:
                print("\u274c  'patterns' is empty! Please ensure variable is defined correctly")
                exit(1)
            print(u'\u2714 "patterns" variable is defined')
        except decouple.UndefinedValueError as patterns_error:
            print("\n\u274c  Variable 'patterns' not defined in .env file")
            print("\nPlease ensure to define the 'patterns' variable")
            exit(1)

    print(u'\u2705 All Environments are defined')


def lfs_checks():
    try:
        lfs_install_check = ["git", "lfs", "--version"]
        p = Popen(lfs_install_check, stdout=PIPE, stderr=PIPE)
        lfs_output, error = p.communicate()
        str_lfs_output = error.decode("utf-8")

        if re.search('is not a git command.+', str_lfs_output):
            print("FATAL: No LFS package was identified on your system, please ensure LFS is installed and run the script again.")
            exit(1)

    except Exception as e:
        print("Error Occurred while validating LFS installation", e)


switch_check()
variable_check()
