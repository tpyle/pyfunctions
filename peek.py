# Reads the next line of a file without 'moving' the cursor
def peek(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line
