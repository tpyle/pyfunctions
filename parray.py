# Pretty Array
# Takes in a string array and returns a pretty string version
def parray ( arr ):
    ret = ""
    if len ( arr ) == 0:
        return ""
    if len ( arr ) == 1:
        return arr[0]
    if len ( arr ) == 2:
        return "{} and {}".format(arr[0],arr[1])
    i = 0
    l = len ( arr )
    for item in arr:
        if ( i == l-2 ):
            ret += "{}, and ".format(item)
        else:
            ret += "{}, ".format(item)
        i += 1
    return ret[:-2]
