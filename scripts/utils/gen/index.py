### Generation helper for index.html

from .. import file as util_file
from .. import csv as util_csv
import shutil


def generate(templatedir, destinationdir, filename):
    """Main generation function for index.html generation helper.

    templatedir -- the relative path of the template html file's directory
    destinationpath -- the directory where index.html should be generated
    filename -- the filename of the index page (always index.html)
    """
    print("- index.py -")

    shutil.copy(f"{templatedir}/{filename}", destinationdir)

    config = util_csv.dictReaderFirstRow("../csv/config.csv")

    for key in config.keys():
        util_file.replaceTextInFile(f"{destinationdir}/{filename}", key, config[key])
