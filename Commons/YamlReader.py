import yaml


def ReadYaml(filePath):
    fileData = None
    with open(filePath, 'r') as yamlFile:
        fileData = yamlFile.read()
    return yaml.load(fileData, Loader=yaml.FullLoader)
