import sys
from colors import colors

# Prints out the string
# Also has pretty printing!
def pwarn ( string ):
    print >> sys.stderr, "{}{}{}".format(colors.YELLOW,string,color.END)
