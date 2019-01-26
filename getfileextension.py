#Retrieves the extension from a file name

def getfileextension(filename):
  loc = filename.rfind['.']
  if loc == -1:
    return None
  return filename[loc+1:]