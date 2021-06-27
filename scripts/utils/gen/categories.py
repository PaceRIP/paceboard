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

    runIdName = "tk_run_id"
    categoryIdName = "tk_category_dashname"
    runs = util_csv.dictReaderMultiRow("../csv/runs.csv", runIdName)
    categories = util_csv.dictReaderMultiRow("../csv/categories.csv", categoryIdName)
    config = util_csv.dictReaderFirstRow("../csv/config.csv")

    for category in categories:

        thisCategory = categories[category]
        path = f"{destinationdir}/{thisCategory[categoryIdName]}"
        currentDir = os.getcwd()

        os.makedirs(path, exist_ok=True)

        shutil.copy(
            f"{currentDir}/{templatedir}/{templateFilename}",
            f"{currentDir}/{path}/index.html",
        )

        for key in thisCategory:
            util_file.replaceTextInFile(f"{path}/index.html", key, thisCategory[key])

        for key in config.keys():
            util_file.replaceTextInFile(f"{path}/index.html", key, config[key])

        ## lk_leaderboard handler ##

        runsInCategory = {}
        for run in runs:
            thisRun = runs[run]
            if (
                thisRun["tk_run_category_dashname"]
                == thisCategory["tk_category_dashname"]
            ):
                runsInCategory[thisRun["tk_run_id"]] = thisRun

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

        sortedRunsInCategory = {
            runId: runDuration
            for runId, runDuration in sorted(
                runDurationsInCategory.items(), key=lambda item: item[1]
            )
        }

        trimmedRunsInCategory = {}
        runnersRepresentedInCategory = []
        for run in sortedRunsInCategory:
            thisRun = runs[run]
            runner = thisRun["tk_run_runner"]
            if runner not in runnersRepresentedInCategory:
                trimmedRunsInCategory[thisRun["tk_run_id"]] = thisRun
            runnersRepresentedInCategory.append(runner)

        place = 1
        lk_leaderboard = '<table class="categoryBoard centerHoriz">'
        for run in trimmedRunsInCategory:

            thisRun = trimmedRunsInCategory[run]
            thisRunner = thisRun["tk_run_runner"]
            thisRunId = thisRun["tk_run_id"]
            thisLink = f"../../runs/{thisRunId}"
            thisDuration = str(runDurationsInCategory[thisRunId])
            thisDate = thisRun["tk_run_date"]

            lk_leaderboard += f'<tr><th>{place}.</th><th>{thisRunner}</th><th><a href="{thisLink}">{thisDuration}</a></th><th>{thisDate}</th></tr>'

            # Also handle replacing lk_run_place on run pages
            util_file.replaceTextInFile(
                f"{destinationdir}/../runs/{thisRunId}/index.html",
                "lk_run_place",
                str(place),
            )

            place += 1

        lk_leaderboard += "</table>"

        util_file.replaceTextInFile(
            f"{path}/index.html", "lk_leaderboard", lk_leaderboard
        )

        ## End of: lk_leaderboard handler ##
