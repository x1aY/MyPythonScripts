import os
from functools import reduce


def GetAbsPath(fileName, *prePaths):
    prePath = reduce(lambda pathA, pathB: os.path.join(pathA, pathB), prePaths)
    return os.path.join(prePath, fileName)
