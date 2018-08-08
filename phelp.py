import sys
import os

###### phelp
# used in printing out the help desciption of a file
# Expects to receive a description, and then an array of tuples, with the first value in the tuple being the command line argument (i.e. -c),
# And the second value being the description of that argument.
# I.e. phelp("some string", [("-c","enables the c flag")]


def phelp(description,clargs):
    print >> sys.stderr, description
    rows, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    maxlength = 0
    for clarg in clargs:
        if len ( clarg[0] ) > maxlength:
            maxlength = len ( clarg[0] )
    maxlength += 2
    width = int(columns/3 - maxlength)
    if columns/3 < 50:
        width = columns-maxlength-8
    for clarg in clargs:
        end = width
        if len ( clarg[1] ) > width:
            end = clarg[1][:width].rfind(' ') + 1
        print >> sys.stderr, "\t{}{}{}".format(clarg[0],(' ' * (maxlength-len(clarg[0]))),clarg[1][:end])
        ci = end
        while ci < len ( clarg[1] ):
            end = ci + width
            if len ( clarg[1] ) > end:
                end = clarg[1][ci:end].rfind(' ') + 1
            print >> sys.stderr, "\t{}{}".format((' ' * maxlength),clarg[1][ci:ci+end])
            ci += end
