import os
import sys
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.append(cwd)
from parse import medline_parser