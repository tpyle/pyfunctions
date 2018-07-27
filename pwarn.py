import sys

# Prints out the string
# Also has pretty printing!
def pwarn ( string ):
    print >> sys.stderr, "{}{}{}".format('\033[93m',string,'\033[0m')
