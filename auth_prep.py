from sys import argv
from os import environ
import decouple
from decouple import Csv
import re

print("######################################")
print("Checking Environment Variables Defined")
print("######################################")

# Used to check if variables is defined appropriately
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
    uname = decouple.config('username')
    if len(uname) <= 0:
        print("\u274c  'username' is empty! Please ensure variable is defined correctly")
        exit(1)
    print(u'\u2714 "username" variable is defined')
except decouple.UndefinedValueError as username_error:
    print("\n\u274c  Variable 'username' not defined in .env file")
    print("\nPlease ensure to define the 'username' variable")
    exit(1)

if re.search('https.+', repo_url):
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

    creds = uname + ":" + pwd
    # Splitting Bitbucket URL into 3, then concatenate CREDS into it.
    http = repo_url[:8]
    bb_domain = repo_url[8:21]
    repo_slug = repo_url[22:]
    full_repo_url = http + creds + "@" + bb_domain + "/" + repo_slug
    # print("https")
    # print(full_repo_url)
# If above statement is false, it assume's the 'repo_url' to be SSH as below
else:
    full_repo_url = repo_url
    # print("SSH")
    # print(full_repo_url)


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

try:
    if decouple.config('Switch_Branch') == 'yes':
        switch_branch = decouple.config('Switch_Branch')
        print(u'\u2714 "Switch_Branch" variable is defined')
        try:
            branch_name = decouple.config('branch_name')
            print(u'\u2714 "branch_name" variable is defined')
            #print(branch_name)

            if len(branch_name) <= 0:
                print("\u274c  You stated that you want to Switch Branch, but branch_name variable is empty")
                exit(1)

        except decouple.UndefinedValueError as branch_name_error:
            print("\n\u274c  Variable 'branch_name' not defined in .env file")
            print("Please ensure to define the 'branch_name' variable")
            exit(1)
    else:
        switch_branch = decouple.config('Switch_Branch')
        if len(switch_branch) < 2:
            print("\u274c  'Switch_Branch' is incorrect! State 'yes' or 'no'")
            exit(1)
        print(u'\u2714 "Switch_Branch" variable is defined')
        #print(switch_branch)
except decouple.UndefinedValueError as branch_name_error:
    print("\n\u274c  Variable 'Switch_Branch' not defined in .env file")
    print("\nPlease ensure to define the 'Switch_Branch' variable")
    exit(1)


print(u'\u2705 All Environments are defined')