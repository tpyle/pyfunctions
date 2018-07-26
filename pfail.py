import sys

# Prints out the string and fails with the optional error code
# Also has pretty printing!
def pfail ( string, code=1 ):
    print >> sys.stderr, "{}{}{}".format('\033[91m',string,'\033[0m')
    sys.exit(code)
