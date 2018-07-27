import sys
from colors import colors

# Prints out the string
# Also has pretty printing!
def psucceed ( string ):
    print >> sys.stderr, "{}{}{}".format(colors.yellow,string,colors.END)
