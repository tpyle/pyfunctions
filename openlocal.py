import os
import inspect

def openlocal( filename, mode ):
    return open ( os.path.join( os.path.dirname ( os.path.relpath( inspect.stack()[1][1],            
                                                                   basePath) ), 
                                filename ), 
                  mode )
