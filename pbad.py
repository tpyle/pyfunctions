import colors
from pcolor import pcolor

# Like pfail, but doen't fail afterwords
def pbad ( string ):
    pcolor ( string, colors.RED )
