#!/usr/bin/env python3
### Main helper script.

import subprocess, os
import scripts.utils.csv as util_csv

os.chdir("scripts/")
cwd = os.getcwd()


def generate():
    """Regenerate site"""
    runIdName = "tk_run_id"
    categoryIdName = "tk_category_dashname"
    runs = util_csv.dictReaderMultiRow("../csv/runs.csv", runIdName)
    categories = util_csv.dictReaderMultiRow("../csv/categories.csv", categoryIdName)
    config = util_csv.dictReaderFirstRow("../csv/config.csv")
    print(len(config))
    print(len(categories))
    print(len(runs))
    if len(config) != 0 and len(categories) != 0 and len(runs) != 0:
        subprocess.call(cwd + "/generate.py", shell=True)


def optionSetup():
    """Reconfigure site details"""
    subprocess.call(cwd + "/setup.py", shell=True)


def optionAddCategory():
    """Add category"""
    subprocess.call(cwd + "/add-category.py", shell=True)


def optionAddRun():
    """Add run"""
    subprocess.call(cwd + "/add-run.py", shell=True)


def optionQuit():
    """Quit"""
    os._exit(1)


# If no setup completed, run setup script
config = util_csv.dictReaderFirstRow("../csv/config.csv")
if len(config) == 0:
    optionSetup()
    generate()

# Set options (as defined earlier)
options = [optionSetup, optionAddCategory, optionAddRun, optionQuit]

# Main loop
while True:
    key = "tk_game_name"
    print(f"\n[ paceboard for {config[key]} ]")
    index = 0
    for option in options:
        print(f"{index + 1} - {options[index].__doc__}")
        index += 1
    try:
        try:
            rawOptionInput = input("Your pick:  ")
        except KeyboardInterrupt:
            os._exit(1)
        optionInput = int(rawOptionInput)
        if 0 < optionInput <= len(options):
            options[optionInput - 1]()
            generate()
        else:
            print("Not a valid choice!")
    except:
        print("Not a valid choice!")
