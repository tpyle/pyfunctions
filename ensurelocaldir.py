import os
import sys
import inspect

def ensurelocaldir(dirname):
    dirpath = os.path.dirname ( os.path.relpath( inspect.getfile(sys._getframe(1))) )
    dirnamepath = os.path.join(dirpath,dirname)
    if not os.path.exists(dirnamepath):
        os.makedirs(dirnamepath)
