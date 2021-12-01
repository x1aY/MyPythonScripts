from flask import Flask
import json
from AutoExtractLec.AutoExtractLecture import AutoExtractLec
from Config.MyConfig import MyConfig
from Commons.PathParser import GetAbsPath

app = Flask(__name__)
devPath = GetAbsPath('dev.yaml', app.root_path, 'Config')
proPath = GetAbsPath('pro.yaml', app.root_path, 'Config')
myConfig = MyConfig(devPath)


@app.route('/')
def defaultPage():
    return 'this is a flask project'


@app.route('/autoExtractLec')
def autoExtractLec():
    return json.dumps(AutoExtractLec(myConfig.myMongoHost, myConfig.myMongoPwd))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=myConfig.myPort)
