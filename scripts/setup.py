#!/usr/bin/env python3
### Initial configuration script for paceboard. Handles adding data to config.csv.

from utils import csv as util_csv

divider = "----------"

print(
    f"\nWelcome to paceboard! Let's set up your leaderboard site :)\nWe'll save this info in csv/config.csv\n\n{divider}\n"
)

# All input handling
tk_game_name = input("Your game's name:  ").replace('"', "")
tk_game_description = input("Description for your game:  ").replace('"', "")
tk_url = input("URL of your site (format - foobar.com):  ")
tk_logo_alt = input(
    "Description of your game's logo (this is used for alt-text):  "
).replace('"', "")

# Define config dictionary
configDict = {
    "tk_game_name": tk_game_name,
    "tk_game_description": tk_game_description,
    "tk_url": tk_url,
    "tk_logo_alt": tk_logo_alt,
}

# Write to csv
util_csv.dictWriter("../csv/config.csv", configDict)

print(f"\n{divider}\n\nPerfect, that's all for now! <3")
