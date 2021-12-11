from flask import Blueprint, request, abort, make_response
import hashlib
from WeChat.ReqParser import ParseData
from Config.MyConfig import MyConfig

WECHAT_TOKEN = MyConfig.wxToken
wxRouter = Blueprint('wxRouter', __name__)


@wxRouter.route('/handler', methods=['GET', 'POST'])
def wechat():
    # 微信的服务器验证
    if request.method == 'GET':
        signature = request.args.get('signature')
        timestamp = request.args.get('timestamp')
        nonce = request.args.get('nonce')
        echostr = request.args.get("echostr")
        if not all([signature, timestamp, nonce]):
            abort(400)
        # 按照微信的流程进行计算签名
        array = [WECHAT_TOKEN, timestamp, nonce]
        array.sort()
        tmp_str = "".join(array)
        sign = hashlib.sha1(tmp_str.encode("utf-8")).hexdigest()
        if signature != sign:
            abort(403)
        else:
            return echostr
    # 数据请求
    elif request.method == 'POST':
        resData = ParseData(request.data)
        print(resData)
        response = make_response(resData)
        response.content_type = 'application/xml'
        return response
