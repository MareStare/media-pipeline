import sys
import os
import importlib

script_dir = os.path.dirname(__file__)
if script_dir not in sys.path:
    sys.path.append(script_dir)

import lib

importlib.reload(lib).run(__file__)
