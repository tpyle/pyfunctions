import sys

# Like pfail, but doen't fail afterwords
def pbad ( string ):
    print >> sys.stderr, "{}{}{}".format('\033[91m',string,'\033[0m')
