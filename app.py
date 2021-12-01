from flask import Flask
import json
from AutoExtractLec.AutoExtractLecture import AutoExtractLec
from Config.MyConfig import MyConfig

myConfig = MyConfig('./Config/dev.yaml')
app = Flask(__name__)


@app.route('/')
def defaultPage():
    return 'this is a flask project'


@app.route('/autoExtractLec')
def autoExtractLec():
    return json.dumps(AutoExtractLec(myConfig.myMongoHost, myConfig.myMongoPwd))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=myConfig.myPort)
