#!/usr/bin/env python3
### Generate all site pages using csv files.

from utils.gen import index as gen_index
from utils.gen import categories as gen_categories
from utils.gen import runs as gen_runs

print("Generating homepage...")
gen_index.generate("../templates", "..", "index.html")

print("Generating details pages for each run...")
gen_runs.generate("../templates", "../runs", "run.html")

print("Generating leaderboard pages for each category...")
gen_categories.generate("../templates", "../categories", "category.html")


print("Done generating site!")
