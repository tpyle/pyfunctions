import sys
from colors import colors

# Like pfail, but doen't fail afterwords
def pbad ( string ):
    print >> sys.stderr, "{}{}{}".format(colors.RED,string,colors.END)
