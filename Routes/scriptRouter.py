from flask import Blueprint, request, abort
from AutoExtractLec.AutoExtractLecture import AutoExtractLec
from Config.MyConfig import MyConfig
from Commons.MyResp import myResp

scriptRouter = Blueprint('scriptRouter', __name__)


@scriptRouter.route('/autoExtractLec', methods=['GET', 'POST'])
def autoExtractLec():
    data = AutoExtractLec(MyConfig.myMongoHost, MyConfig.myMongoPwd)
    return myResp(data), 200
