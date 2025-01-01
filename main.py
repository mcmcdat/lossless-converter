import os
import sys

from utils import converter

path = sys.argv[1]
delete = (sys.argv[2].lower()=='true')
recursive = (sys.argv[3].lower()=='true')

if os.path.exists(path):
    print(f"Converting files from {path}, where delete = {delete} and recursive = {recursive}.")
    go = input(f"Proceed? (y/n):")
    if ((go.lower() == "yes") | (go.lower() == "y")):
        converter.convert_to_mp3(sys.argv[1],
                                delete_original=delete,
                                recursive=recursive)
    else:
        print("Task killed")
else:
    print(f"Path '{path}' not found!")