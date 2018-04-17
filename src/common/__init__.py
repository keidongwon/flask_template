# -*- coding: utf-8 -*-
import os
import sys
import json

# add working path
_curpath = os.path.dirname(os.getcwd()) + "/src"
sys.path.append(_curpath)

# add library path (PYTHONPATH)
pathfile = open(_curpath + "/data/libpath.json")
_libpath = json.loads(pathfile.read())
sys.path.append(_libpath['path'])

# ignore next PEP8 import warning
from pybolt.util.filebase import FileBase
from pybolt.platform.version import Version

# create instance
config = FileBase()
errorcode = FileBase()
version = Version()
