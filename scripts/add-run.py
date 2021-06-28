#!/usr/bin/env python3
### Script for adding a new category. Handles adding data to config.csv.

from utils import csv as util_csv
import os

## Check to see if there's at least one category ##

categoriesOld = util_csv.dictReaderMultiRow(
    "../csv/categories.csv", "tk_category_dashname"
)
if len(categoriesOld.keys()) == 0:
    print("Add a category first!")
    os._exit(1)

## End of: Check to see if there's at least one category ##

divider = "----------"

print(
    f"\nWe'll ask for the runner, verifier, run duration (time), category, run date, category, description of, and recording link of the new run.\n\n{divider}\n"
)

tk_run_id = 1
existingRuns = util_csv.dictReaderMultiRow("../csv/runs.csv", "tk_run_id")
for id in existingRuns:
    tk_run_id = int(id) + 1

# Handle input of tk_run_runner and tk_run_verifier
tk_run_runner = input("Runner:  ").replace('"', "")
tk_run_verifier = input("Verifier:  ").replace('"', "")

## Handle input of tk_run_duration ##

doneDurationInput = False
while not doneDurationInput:
    tk_run_duration = input("Duration (format - HH:MM:SS):  ")
    values = tk_run_duration.split(":")
    if len(values) == 3:
        try:
            for value in values:
                test = float(value)
            doneDurationInput = True
        except:
            print("Invalid input!")
    else:
        print("Invalid input!")

## End of: Handle input of tk_run_duration ##

## Handle input of tk_run_category_dashname ##

doneCategoryInput = False
displayName = "tk_category_name"
while not doneCategoryInput:
    print("\nCategory (input a number)")

    index = 0
    categoriesNew = {}
    for category in categoriesOld:
        categoriesNew[index] = categoriesOld[category]
        print(f"{index + 1} - {categoriesNew[index][displayName]}")
        index += 1

    try:
        try:
            rawCategoryInput = input("Your pick:  ")
        except KeyboardInterrupt:
            os._exit(1)
        categoryInput = int(rawCategoryInput) - 1
        if categoryInput <= index:
            try:
                tk_run_category_dashname = categoriesNew[categoryInput][
                    "tk_category_dashname"
                ]
                doneCategoryInput = True
            except:
                print("Not a valid choice!")
        else:
            print("Not a valid choice!")
    except:
        print("Not a valid choice!")
print(f"You picked - {categoriesNew[categoryInput][displayName]}\n")

## End of: Handle input of tk_run_category_dashname ##

# Handle input of tk_run_date, tk_run_description, and tk_run_link
tk_run_date = input("Date (format - MM/DD/YYYY):  ").replace('"', "")
tk_run_description = input("Description:  ").replace('"', "")
tk_run_link = input("Recording link (format - https://foo.bar):  ")

# Define run dictionary
runDict = {
    "tk_run_id": tk_run_id,
    "tk_run_runner": tk_run_runner,
    "tk_run_verifier": tk_run_verifier,
    "tk_run_duration": tk_run_duration,
    "tk_run_category_dashname": tk_run_category_dashname,
    "tk_run_date": tk_run_date,
    "tk_run_description": tk_run_description,
    "tk_run_link": tk_run_link,
}

# Write to csv
util_csv.dictWriter("../csv/runs.csv", runDict, "a")

print(
    f"\n{divider}\n\nAdded run! If you made a mistake, you can manually edit csv/runs.csv"
)
