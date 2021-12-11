from flask import Blueprint, request, abort, make_response
import json
from AutoExtractLec.AutoExtractLecture import AutoExtractLec
from Config.MyConfig import MyConfig

scriptRouter = Blueprint('scriptRouter', __name__)


@scriptRouter.route('/autoExtractLec', methods=['GET', 'POST'])
def autoExtractLec():
    return json.dumps(AutoExtractLec(MyConfig.myMongoHost, MyConfig.myMongoPwd))
