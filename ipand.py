# Computes the bitwise AND of an IP address and Subnet mask
def ipand ( ip, mask ):
    ipparts = ip.split('.')
    mparts = mask.split('.')
    return "{}.{}.{}.{}".format(int(ipparts[0]) & int(mparts[0]),
                                int(ipparts[1]) & int(mparts[1]),
                                int(ipparts[2]) & int(mparts[2]),
                                int(ipparts[3]) & int(mparts[3]))
