import sys
import os

###### phelp
# used in printing out the help desciption of a file
# Expects to receive a description, and then an array of tuples, with the first value in the tuple being the command line argument (i.e. -c),
# And the second value being the description of that argument.
# I.e. phelp("some string", [("-c","enables the c flag")]


def phelp(description,clargs=[],portion=40,indent=4,maxwidth=None):
    preface = ' ' * indent
    if maxwidth == 0:
        maxwidth = None
    if portion == 0:
        portion = 40
    # Compute the width of the screen currently
    rows, columns = os.popen('stty size', 'r').read().split()
    columns = int(columns)
    maxlength = 0
    for clarg in clargs:
        if len ( clarg[0] ) > maxlength:
            maxlength = len ( clarg[0] )
    maxlength += 2
    # print the description
    i = 0
    dwidth = int(columns*portion/100)
    if dwidth < 80:
        dwidth = min ( 80, columns )
    if maxwidth != None:
        dwidth = min ( dwidth, min ( maxwidth, columns ) )
    width = dwidth - indent - maxlength
    while i < len ( description ):
        end = i + dwidth
        if len ( description ) > end:
            end = description[i:end].rfind(' ') +1
            if end == 0:
                end = dwidth
        print >> sys.stderr, description[i:i+end]
        i += end
    # Print arguments
    for clarg in clargs:
        # Figure how much of the first line to print
        end = width
        if len ( clarg[1] ) > width:
            end = clarg[1][:width].rfind(' ') + 1
            if end == 0:
                end = width
        # Print first line
        print >> sys.stderr, "{}{}{}{}".format(preface,clarg[0],(' ' * (maxlength-len(clarg[0]))),clarg[1][:end])
        # print the rest of the lines
        ci = end
        while ci < len ( clarg[1] ):
            end = ci + width
            if len ( clarg[1] ) > end:
                end = clarg[1][ci:end].rfind(' ') + 1
                if end == 0:
                    end = width
            print >> sys.stderr, "{}{}{}".format(preface,(' ' * maxlength),clarg[1][ci:ci+end])
            ci += end
