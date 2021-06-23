### Util library for general file handling


def replaceTextInFile(filepath, oldText, newText):
    file = open(filepath, "rt")
    newFile = file.read().replace(oldText, newText)
    file.close()
    file = open(filepath, "wt")
    file.write(newFile)
    file.close
