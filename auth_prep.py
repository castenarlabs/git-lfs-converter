from sys import argv
from os import environ
import decouple
from decouple import Csv
import re

# Used to check if variables is defined appropriately
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

try:
    if decouple.config('Switch_Branch') == 'yes':
        switch_branch = decouple.config('Switch_Branch')
        try:
            branch_name = decouple.config('branch_name')
            #print(branch_name)

            if len(branch_name) <= 0:
                print("You stated that you want to Switch Branch, but branch_name variable is empty")
                exit(1)

        except decouple.UndefinedValueError as branch_name_error:
            print("\nVariable 'branch_name' not defined in .env file")
            print("Please ensure to define the 'branch_name' variable")
            exit(1)
    else:
        switch_branch = decouple.config('Switch_Branch')
        #print(switch_branch)
except decouple.UndefinedValueError as branch_name_error:
    print("\nVariable 'Switch_Branch' not defined in .env file")
    print("\nPlease ensure to define the 'Switch_Branch' variable")
    exit(1)


# repo_url = decouple.config('repo_url')
# repo_path = decouple.config('repo_path')
# uname = decouple.config('username')


if re.search('https.+', repo_url):
    try:
        pwd = decouple.config('app_password')
    except decouple.UndefinedValueError as app_password_error:
        print("\nVariable 'app_password' not defined in .env file")
        print("\nPlease ensure to define the 'app_password' variable")
        exit(1)
    creds = uname + ":" + pwd
    # Splitting Bitbucket URL into 3, then concatenate CREDS into it.
    http = repo_url[:8]
    bb_domain = repo_url[8:21]
    repo_slug = repo_url[22:]
    full_repo_url = http + creds + "@" + bb_domain + "/" + repo_slug
    # print("https")
    # print(full_repo_url)
else:
    full_repo_url = repo_url
    # print("SSH")
    # print(full_repo_url)
