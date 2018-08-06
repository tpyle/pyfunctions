# prints a task, i.e. A name followed by ** until the end of the screen
import os
import sys

def ptask(string):
    rows,columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    print >> sys.stderr, "TASK [{}] {}".format(string,"*" * (columns-(len(string)%columns)-8))
