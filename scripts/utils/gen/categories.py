### Generation helper for category pages

from .. import file as util_file
from .. import csv as util_csv
import shutil, os, datetime


def generate(templatedir, destinationdir, templateFilename):
    """Main generation function for category page generation helper.

    templatedir -- the relative path of the template html file's directory\n
    destinationpath -- the directory where category paths should be generated\n
    templateFilename -- the filename of the category template (always category.html)\n
    """

    # Read runs, categories, and config csv files
    runIdName = "tk_run_id"
    categoryIdName = "tk_category_dashname"
    runs = util_csv.dictReaderMultiRow("../csv/runs.csv", runIdName)
    categories = util_csv.dictReaderMultiRow("../csv/categories.csv", categoryIdName)
    config = util_csv.dictReaderFirstRow("../csv/config.csv")

    for category in categories:

        # Get proper directory
        thisCategory = categories[category]
        path = f"{destinationdir}/{thisCategory[categoryIdName]}"
        currentDir = os.getcwd()

        # Copy template to appropriate directory
        os.makedirs(path, exist_ok=True)
        shutil.copy(
            f"{currentDir}/{templatedir}/{templateFilename}",
            f"{currentDir}/{path}/index.html",
        )

        # Replace category tk placeholders with values
        for key in thisCategory:
            util_file.replaceTextInFile(f"{path}/index.html", key, thisCategory[key])

        # Replace config tk placeholders with values
        for key in config.keys():
            util_file.replaceTextInFile(f"{path}/index.html", key, config[key])

        ## lk_leaderboard handler ##

        # Find runsInCategory
        runsInCategory = {}
        for run in runs:
            thisRun = runs[run]
            if (
                thisRun["tk_run_category_dashname"]
                == thisCategory["tk_category_dashname"]
            ):
                runsInCategory[thisRun["tk_run_id"]] = thisRun

        # Find runDurationsInCategory by parsing runsInCategory values
        runDurationsInCategory = {}
        for run in runsInCategory:
            thisRun = runsInCategory[run]
            runDurationSplit = [
                float(value) for value in thisRun["tk_run_duration"].split(":")
            ]
            runDurationsInCategory[thisRun["tk_run_id"]] = datetime.timedelta(
                hours=runDurationSplit[0],
                minutes=runDurationSplit[1],
                seconds=runDurationSplit[2],
            )

        # Find sortedRunsInCategory by sorting durations from runDurationsInCategory
        sortedRunsInCategory = {
            runId: runDuration
            for runId, runDuration in sorted(
                runDurationsInCategory.items(), key=lambda item: item[1]
            )
        }

        # Find trimmedRunsInCategory by only including one run per runner from sortedRunsInCategory
        trimmedRunsInCategory = []
        runnersRepresentedInCategory = []
        for run in sortedRunsInCategory:
            thisRun = runs[run]
            runner = thisRun["tk_run_runner"]
            if runner not in runnersRepresentedInCategory:
                trimmedRunsInCategory.append(thisRun)
            runnersRepresentedInCategory.append(runner)

        # Replace lk_leaderboard with category leaderboard table
        place = 1
        lk_leaderboard = '<table class="categoryBoard centerHoriz">'
        for run in trimmedRunsInCategory:

            # Define values for table
            runner = run["tk_run_runner"]
            runId = run["tk_run_id"]
            runLink = f"../../runs/{runId}"
            runDuration = str(runDurationsInCategory[runId])
            runDate = run["tk_run_date"]

            # Concatenate a row to the table
            lk_leaderboard += f'<tr><td>{place}.</td><td>{runner}</td><td><a href="{runLink}">{runDuration}</a></td><td>{runDate}</td></tr>'

            # Also handle replacing lk_run_place on run pages
            util_file.replaceTextInFile(
                f"{destinationdir}/../runs/{runId}/index.html",
                "lk_run_place",
                str(place),
            )

            place += 1
        lk_leaderboard += "</table>"

        # Replace lk_leaderboard placeholder with table string
        util_file.replaceTextInFile(
            f"{path}/index.html", "lk_leaderboard", lk_leaderboard
        )

        ## End of: lk_leaderboard handler ##
