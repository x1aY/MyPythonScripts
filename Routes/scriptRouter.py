from flask import Blueprint, request, abort
from Config.MyConfig import MyConfig
from Commons.MyResp import myResp
from AutoExtractLec.AutoExtractLecture import AutoExtractLec
from Blog.MyBlog import GetBlogListByPage

scriptRouter = Blueprint('scriptRouter', __name__)


@scriptRouter.route('/autoExtractLec', methods=['GET', 'POST'])
def autoExtractLec():
    data = AutoExtractLec(MyConfig.myMongoHost, MyConfig.myMongoPwd)
    return myResp(data), 200


@scriptRouter.route('/blogList', methods=['GET', 'POST'])
def blogList():
    page, perPage = request.json.get('page'), request.json.get('perPage')
    totalPage, blogList = GetBlogListByPage(MyConfig.myMongoHost, MyConfig.myMongoPwd, page, perPage)
    return myResp({"totalPage": totalPage, "blogList": blogList}), 200
