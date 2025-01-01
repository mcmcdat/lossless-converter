# Should take in arguments for
# 1) whether to delete old files or not (default do not),
# 2) path to songs
# 3) recursive convert or not

import os
import sys

from utils import converter

path = sys.argv[1]

delete = (sys.argv[2].lower()=='true')
recursive = (sys.argv[3].lower()=='true')

converter.convert_to_mp3(sys.argv[1],
                         delete_original=delete,
                         recursive=recursive)