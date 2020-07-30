from sys import argv
from os import environ
import decouple
from decouple import Csv
import re


def auth_prep():
    repo_url = decouple.config('repo_url')
    repo_path = decouple.config('repo_path')
    uname = decouple.config('username')

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
