from sys import argv
from os import environ
import decouple
from decouple import Csv
import re

repo_url = decouple.config('repo_url')
repo_path = decouple.config('repo_path')
uname = decouple.config('username')
pwd = decouple.config('app_password')
creds = uname + ":" + pwd

if re.search('https.+', repo_url):
    # Splitting Bitbucket URL into 3, then concatenate CREDS into it.
    http = repo_url[:8]
    bb_domain = repo_url[8:21]
    repo_slug = repo_url[22:]
    full_repo_url = http + creds + "@" + bb_domain + "/" + repo_slug
    # print("https")
    #print(full_repo_url)
else:
    full_repo_url = repo_urls
    # print("SSH")
    #print(full_repo_url)
