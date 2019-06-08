import sys
from .pbad import pbad

# Prints out the string and fails with the optional error code
# Also has pretty printing!
def pfail ( string, code=1 ):
    pbad ( string )
    sys.exit(code)
