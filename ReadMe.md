# This program is to automate conversion of Existing Repositories to LFS

****
* This Script Supports Conversion to LFS via :

    * Directory
    * Patterns
   
### **What is required!**
1. GIT (Latest Version Preferably) Installed

1. GIT LFS Installed

1. Python 3 Installed & Packages in requirements.txt installed

1. .env file following the [template](https://bitbucket.org/castenar/automated-lfs-converter/src/master/.env-template)

    * Refer to example below
   
#### Authentication
1. Method of clone via SSH OR HTTPS will be determined based on URL used on .env file

   1. If you use a HTTPS URL : 
      1. In .env file, you will need a bb_username and bb_app_password variable
   1. If you use SSH URL
      1. You will be prompted for your SSH Key credentials 
      1. Alternatively you can add your SSH Key to the SSH Agent
   
### **Sample .env file**

      # USE HTTPS OR SSH URL (either one)
      repo_url = "<Repository URL>"

      # LOCAL PATHS of where the cloned repository will be located (/Users/trichard/Documents/Python/CLONE_REPO/).
      # This directory should be empty
      repo_path = "<path to your local repo directory>"

      # CREDENTIALS (Only for HTTPS)
      bb_username = "<username>"
      bb_app_password = "<password>"

      #Define patterns AND/OR folder separated by comma (,) E.g : `Patterns=py,jpg,png` | Folder=notebook,script/file_handler
      patterns=<patterns>
      folder=<folder>

### **What you need to do**
1. Ensure Requirements above are met.
1. Run script : `main.py`


### **How it works**
1. Read and validate .env file to ensure variables are defined

1. Removes existing clone directory if exists from specified path (Please ensure it's empty)

1. Looks for specified clone directory with "_backup" appended to it. If exists, it will be removed.

1. Makes a mirror clone of the repository in the specified directory  

1. Takes Repository Backup in the same directory mentioned
   
1. Initializes LFS in the repo 
   
1. Converts to LFS using "GIT LFS MIGRATE" 

1. Runs GIT GC Aggressive
   
1. User have the option to FORCE PUSH back to remote OR force push manually later

1. After the push within script, a Summary will be printed.
