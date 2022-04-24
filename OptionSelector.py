import optparse
import sys
from optparse import OptionParser



#required = "username password local_path repo_url".split()
#either_one = ['patterns', 'folder', 'size']
either_one = ['patterns', 'folder']
parser = OptionParser()


def parse_input():
    """
    Reads in attributes during run time and sets usage flags appropriately.
    """
    # parser = OptionParser()
    # Required Flag
    #parser.add_option('-u', '--user', dest='username', default=None, action="store", help="[REQUIRED] User which has WRITE permission to the repository", )
    #parser.add_option('-c', '--pass', dest='password', default=None, action="store", help="[REQUIRED] App_Password which has WRITE permission to the repository", )
    parser.add_option('-p', '--pattern', dest='patterns', default=None, action="store_true", help="[REQUIRED] File  patterns to be converted to LFS (png,jpg)")
    #parser.add_option('-p', '--pattern', dest='patterns', default=None, action="store", help="[REQUIRED] File  patterns to be converted to LFS (png,jpg)")
    parser.add_option('-f', '--folder', dest='folder', default=None, action="store_true", help="[REQUIRED] Convert all files in a directory to LFS (folder1, folder2)")
    #parser.add_option('-s', '--size', dest='size', default=None, action="store", help="[REQUIRED] Sets verbose logging to enabled")
    #parser.add_option('-l', '--local-path', dest='local_path', default=None, action="store", help="[REQUIRED] Local full path of where clone will be stored")
    #parser.add_option('-r', '--repo-url', dest='repo_url', default=None, action="store", help="[REQUIRED] Local full path of where clone will be stored")

    #Optional Flag
    #parser.add_option('-d', '--dry-run', dest='dryrun', default=False, action="store_true", help='Flag dry-run only, no write operations.')

    options, args = parser.parse_args()
    return options, args


# Seems like Option Parse calls sysexit on error.
try:
    options, args = parse_input()
except (optparse.OptionConflictError, optparse.BadOptionError, optparse.OptionError) as err:
    print("HELP", err)


def switch_check():
    #for r in required:
    #    while options.__dict__[r] is None:
    #        print("Parameter Missing :", r, '\n')
    #        parser.error("Parameter %s required" % required)

    if options.__dict__['folder'] and options.__dict__['patterns']:
        print("Folder option   : ", options.__dict__['folder'], "\nPattern option  : ", options.__dict__['patterns'])
        print("You have used the option to convert all files by matching patterns and all files in defined folders to LFS")
        pass
    elif options.__dict__['folder']:
        print("Folder option:", options.__dict__['folder'])
        print("You have used the option to convert all files in defined folders to LFS")
        pass
    elif options.__dict__['patterns']:
        print("Pattern Option", options.__dict__['patterns'])
        print("You have used the option to convert files by matching pattern to LFS")
        pass
    # elif options.__dict__['size']:
        pass
    else:
        print('All or either one of this option is required.', either_one, '. Use "-h" for more information')
        exit(1)


#switch_check()
