from Commons.YamlReader import ReadYaml


class MyConfig:
    debug = True

    myPort = 5000

    myMongoHost = 'localhost'

    myMongoPwd = ''

    def __init__(self, envPath):
        yamlData = ReadYaml(envPath)
        self.debug = yamlData['debug']
        self.myPort = yamlData['myPort']
        self.myMongoHost = yamlData['myMongoHost']
        self.myMongoPwd = yamlData['myMongoPwd']
