import os
import sys
import inspect

def openlocal( filename, mode ):
    return open ( os.path.join( os.path.dirname ( os.path.relpath( inspect.getfile(sys._getframe(1))) ), 
                                filename ), 
                  mode )
