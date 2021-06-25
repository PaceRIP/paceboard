### Util library for general file handling


def replaceTextInFile(filepath, oldText, newText):
    """Replace all occurrences of some text in plaintext file with some other text.

    filepath -- the path of the plaintext file\n
    oldText -- the text to replace\n
    newText -- the text to implement\n
    """
    file = open(filepath, "rt")
    newFile = file.read().replace(oldText, newText)
    file.close()
    file = open(filepath, "wt")
    file.write(newFile)
    file.close
