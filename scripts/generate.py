### Generate all site pages using csv files.

from utils.gen import index as gen_index
from utils.gen import categories as gen_categories
from utils.gen import runs as gen_runs

gen_index.generate()
gen_categories.generate()
gen_runs.generate()

print("Done generating site!")
