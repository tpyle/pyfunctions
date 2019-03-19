import sys
import colors

def pcolor(string,color):
    print >> sys.stderr, u"{}{}{}".format(color, string, colors.END)
