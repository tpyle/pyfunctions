import os

def getallfiles(dir_path):
  _files = os.listdir(dir_path)
  allFiles = list()
  for entry in _files:
    fullPath = os.path.join(dir_path, entry)
    if os.path.isdir(fullPath):
      allFiles = allFiles + getallfiles(fullPath)
    else:
      allFiles.append(fullPath)
  return allFiles