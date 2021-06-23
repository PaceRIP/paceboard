### Initial configuration script for paceboard. Handles adding properties to config.csv.

from utils import csv as util_csv

divider = "----------"

print(
    "\nWelcome to paceboard! Let's set up your leaderboard site :)\nWe'll save this info in csv/config.csv\n\n"
    + divider
    + "\n"
)

tk_game = input("Your game's name:  ")
tk_description = input("Description for your game:  ")
tk_url = input("URL of your site (format example - foobar.com):  ")
tk_logo_alt = input("Description of your game's logo (this is used for alt-text):  ")

print(
    "\n"
    + divider
    + "\n\nPerfect! You can always overwrite the info above by running this script again.\nHere's an overview of how to use paceboard:\n\n- Add a category using scripts/add-category.py\n- Add a run using scripts/add-run.py\n- Use scripts/generate.py to update the site with the info you've added.\n- All categories, runs, and configuration details are stored in csv/\n- Replace the logo saved as assets/img/logo.png\n- For the adventurous, you can restyle your site's pages by editing files within templates/ and css/\n\nRemember to run scripts/generate.py to initialize your site.\nThat's all for now! <3\n"
)

util_csv.findFile()
