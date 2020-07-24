from sys import argv
from os import environ
import decouple
from decouple import Csv

https_repo_url = decouple.config('https_repo_url')
repo_path = decouple.config('repo_path')
uname = decouple.config('username')
pwd = decouple.config('app_password')
creds = uname + ":" + pwd
#print(creds)


http = https_repo_url[:8]
bb_domain = https_repo_url[8:21]
repo_slug = https_repo_url[22:]

full_repo_url = http + creds + "@" + bb_domain + "/" + repo_slug
print(full_repo_url)


#if argv[1] == "Username for 'https://github.com': ":
   # print (environ['GIT_USERNAME'])
   # exit()

#if argv[1] == "Password for 'https://%(GIT_USERNAME)s@github.com': " % environ:
 #   print(environ['GIT_PASSWORD'])
  #  exit()

#path.clone(is_bare=True)
