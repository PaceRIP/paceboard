### Script for adding a new category. Handles adding data to config.csv.

from utils import csv as util_csv

divider = "----------"

print(
    f"\nWe'll ask for the name, description, and rules of the new category.\n\n{divider}\n"
)

tk_category_name = input("Name:  ")
tk_category_description = input("Description:  ")
tk_category_rules = input("Rules:  ")

tk_category_dashname = tk_category_name.replace(" ", "_")

categoryDict = {
    "tk_category_dashname": tk_category_dashname,
    "tk_category_name": tk_category_name,
    "tk_category_description": tk_category_description,
    "tk_category_rules": tk_category_rules,
}

util_csv.dictWriter("../csv/categories.csv", categoryDict, "a")

print(
    f"\n{divider}\n\nAdded category! If you made a mistake, you can manually edit csv/categories.csv (and csv/runs.csv if you've added any runs to the borked category). \n"
)
