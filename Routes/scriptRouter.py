from flask import Blueprint, request, abort
from Config.MyConfig import MyConfig
from Commons.MyResp import myResp
from AutoExtractLec.AutoExtractLecture import AutoExtractLec
from Blog.MyBlog import GetBlogListByPage, GetBlogListInfo

scriptRouter = Blueprint('scriptRouter', __name__)


@scriptRouter.route('/autoExtractLec', methods=['GET', 'POST'])
def autoExtractLec():
    data = AutoExtractLec(MyConfig.myMongoHost, MyConfig.myMongoPwd)
    return myResp(data), 200


@scriptRouter.route('/blogBaseInfo', methods=['GET', 'POST'])
def blogBaseInfo():
    perPage = request.json.get('perPage')
    count, totalPage = GetBlogListInfo(MyConfig.myMongoHost, MyConfig.myMongoPwd, perPage)
    return myResp({"totalBlog": count, "totalPage": totalPage}), 200


@scriptRouter.route('/blogList', methods=['GET', 'POST'])
def blogList():
    page, perPage = request.json.get('page'), request.json.get('perPage')
    blogPage = GetBlogListByPage(MyConfig.myMongoHost, MyConfig.myMongoPwd, page, perPage)
    return myResp({"blogList": blogPage}), 200
