# -*- coding: utf-8 -*-
import os
import sys
import json

uppath = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])

# add working path
# _curpath = os.path.dirname(os.getcwd()) + "/src"
_curpath = os.path.dirname(os.path.abspath(__file__))
_curpath = uppath(_curpath, 1)
sys.path.append(_curpath)

# add library path (PYTHONPATH)
pathfile = open(_curpath + "/data/libpath.json")
_libpath = json.loads(pathfile.read())
sys.path.append(_libpath['path'])

# ignore next PEP8 import warning
from pybolt.util.filebase import FileBase

# create instance
config = FileBase()
errorcode = FileBase()
config.load(FilePrefix.CONFIG, _curpath+"/data")
