#!/usr/bin/env python3
### Main helper script.

import subprocess, os
import scripts.utils.csv as util_csv

# If no setup completed, run setup script
config = util_csv.dictReaderFirstRow("csv/config.csv")
if config == {}:
    subprocess.call("scripts/setup.py", shell=True)

doneOptionInput = False


def optionSetup():
    """Reconfigure site details"""
    print("hi")


def optionAddCategory():
    """Add category"""
    print("hello")


def optionAddRun():
    """Add run"""
    print("cool")


def optionQuit():
    """Quit"""
    os._exit(1)


options = [optionSetup, optionAddCategory, optionAddRun, optionQuit]

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
            print("")
            options[optionInput - 1]()
        else:
            print("Not a valid choice!")
    except:
        print("Not a valid choice!")
