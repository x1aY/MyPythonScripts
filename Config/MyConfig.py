from Commons.YamlReader import ReadYaml


class MyConfig:
    debug = True

    myPort = 5000

    myMongoHost = 'localhost'

    myMongoPwd = ''

    wxToken = ''

    @classmethod
    def initConfig(cls, envPath):
        yamlData = ReadYaml(envPath)
        cls.debug = yamlData['debug']
        cls.myPort = yamlData['myPort']
        cls.myMongoHost = yamlData['myMongoHost']
        cls.myMongoPwd = yamlData['myMongoPwd']
        cls.wxToken = yamlData['wxToken']
