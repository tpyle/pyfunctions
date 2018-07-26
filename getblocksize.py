# Converts a subnet in N.N.N.N format to /N (i.e. 255.255.255.0 -> 24)
def getblocksize ( mask ):
    mparts = mask.split('.')
    s = 0
    for num in mparts:
        s = s + bin(int(num)).count("1")
    return s
