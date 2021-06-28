### Generation helper for run pages

from .. import file as util_file
from .. import csv as util_csv
import shutil, os, datetime


def generate(templatedir, destinationdir, templateFilename):
    """Main generation function for run page generation helper.

    templatedir -- the relative path of the template html file's directory\n
    destinationpath -- the directory where run paths should be generated\n
    templateFilename -- the filename of the run template (always run.html)\n
    """

    # Read runs, categories, and config csv files
    runIdName = "tk_run_id"
    categoryIdName = "tk_category_dashname"
    runs = util_csv.dictReaderMultiRow("../csv/runs.csv", runIdName)
    categories = util_csv.dictReaderMultiRow("../csv/categories.csv", categoryIdName)
    config = util_csv.dictReaderFirstRow("../csv/config.csv")

    for run in runs:

        # Get proper directory
        thisRun = runs[run]
        path = f"{destinationdir}/{thisRun[runIdName]}"
        currentDir = os.getcwd()

        # Copy template to appropriate directory
        os.makedirs(path, exist_ok=True)
        shutil.copy(
            f"{currentDir}/{templatedir}/{templateFilename}",
            f"{currentDir}/{path}/index.html",
        )

        # Replace run tk placeholders with values, then save tk_run_link and tk_run_duration for use in lk handlers
        tk_run_link = ""
        for key in thisRun:
            util_file.replaceTextInFile(f"{path}/index.html", key, thisRun[key])
            if key == "tk_run_link":
                tk_run_link = thisRun[key]
            elif key == "tk_run_duration":
                tk_run_duration = thisRun[key]

        # Replace category tk placeholders with values
        for key in categories[thisRun["tk_run_category_dashname"]]:
            util_file.replaceTextInFile(
                f"{path}/index.html",
                key,
                categories[thisRun["tk_run_category_dashname"]][key],
            )

        # Replace config tk placeholders with values
        for key in config.keys():
            util_file.replaceTextInFile(f"{path}/index.html", key, config[key])

        # lk_run_link handler
        if tk_run_link == "":
            util_file.replaceTextInFile(
                f"{path}/index.html", "lk_run_link", "No recording available"
            )
        else:
            util_file.replaceTextInFile(
                f"{path}/index.html",
                "lk_run_link",
                f'<a class="runLink" href="{tk_run_link}">Run recording</a>',
            )

        # lk_run_duration handler
        runDurationSplit = [float(value) for value in tk_run_duration.split(":")]
        lk_run_duration = datetime.timedelta(
            hours=runDurationSplit[0],
            minutes=runDurationSplit[1],
            seconds=runDurationSplit[2],
        )
        util_file.replaceTextInFile(
            f"{path}/index.html", "lk_run_duration", str(lk_run_duration)
        )
