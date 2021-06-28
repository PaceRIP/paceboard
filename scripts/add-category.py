#!/usr/bin/env python3
### Script for adding a new category. Handles adding data to config.csv.

from utils import csv as util_csv

divider = "----------"

print(f"\nWe'll ask for the name and rules of the new category.\n\n{divider}\n")

# All input handling
tk_category_name = input("Name:  ").replace('"', "")
tk_category_rules = input("Rules:  ").replace('"', "")

# Generate dashname (specifically for directory names)
tk_category_dashname = tk_category_name.replace(" ", "_").replace("%", "")

# Define category dictionary
categoryDict = {
    "tk_category_dashname": tk_category_dashname,
    "tk_category_name": tk_category_name,
    "tk_category_rules": tk_category_rules,
}

# Write to csv
util_csv.dictWriter("../csv/categories.csv", categoryDict, "a")

print(
    f"\n{divider}\n\nAdded category! If you made a mistake, you can manually edit csv/categories.csv (and csv/runs.csv if you've added any runs to the borked category)."
)
