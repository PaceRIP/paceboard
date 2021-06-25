### Generation helper for category pages

from .. import file as util_file
from .. import csv as util_csv
import shutil
import os


def generate(templatedir, destinationdir, templateFilename):
    """Main generation function for category page generation helper.

    templatedir -- the relative path of the template html file's directory
    destinationpath -- the directory where category paths should be generated
    filename -- the filename of the category template (always category.html)
    """

    idName = "tk_category_dashname"
    categories = util_csv.dictReaderMultiRow("../csv/categories.csv", idName)
    config = util_csv.dictReaderFirstRow("../csv/config.csv")

    for category in categories:

        path = f"{destinationdir}/{categories[category][idName]}"
        currentDir = os.getcwd()

        os.makedirs(path, exist_ok=True)

        shutil.copy(
            f"{currentDir}/{templatedir}/{templateFilename}",
            f"{currentDir}/{path}/index.html",
        )

        for key in categories[category]:
            util_file.replaceTextInFile(
                f"{path}/index.html", key, categories[category][key]
            )

        for key in config.keys():
            util_file.replaceTextInFile(f"{path}/index.html", key, config[key])
