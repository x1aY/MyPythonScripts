import os
from functools import reduce
from flask import current_app


def GetPath(fileName, *prePaths):
    prePath = reduce(lambda pathA, pathB: os.path.join(pathA, pathB), prePaths)
    return os.path.join(prePath, fileName)


devPath = GetPath('dev.yaml', current_app.root_path, 'Config')
proPath = GetPath('pro.yaml', current_app.root_path, 'Config')
