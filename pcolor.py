import sys
from colors import colors

def pcolor(string,color):
    print >> sys.stderr, '{}{}{}'.format(color, string, colors.ENDC)
