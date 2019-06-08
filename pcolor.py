import sys
from . import colors

def pcolor(string,color):
    print("{}{}{}".format(color, string, colors.END), file=sys.stderr)
