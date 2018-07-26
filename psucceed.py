import sys

# Prints out the string
# Also has pretty printing!
def psucceed ( string ):
    print >> sys.stderr, "{}{}{}".format('\033[92m',string,'\033[0m')
