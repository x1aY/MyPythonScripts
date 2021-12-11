import xmltodict
import time
from WeChat.ContentParser import ParseByMsgType


def GetDataDict(data):
    return xmltodict.parse(data).get('xml')


def GetResponseXml(MsgType, ToUserName, FromUserName,
                   Content="I don't know what you're talking about"):
    responseDict = {
        "xml": {
            "ToUserName": ToUserName,
            "FromUserName": FromUserName,
            "CreateTime": int(time.time()),
            "MsgType": "text",
            "Content": Content
        }
    }
    return xmltodict.unparse(responseDict)


def ParseData(data):
    xmlDict = GetDataDict(data)
    # CreateTime = xmlDict.get('CreateTime')
    # MsgId = xmlDict.get('MsgId')
    ToUserName = xmlDict.get('ToUserName')
    FromUserName = xmlDict.get('FromUserName')
    MsgType = xmlDict.get('MsgType')
    Content = xmlDict.get('Content')
    resContent = ParseByMsgType(MsgType, Content, xmlDict)
    responseDict = GetResponseXml(MsgType, FromUserName, ToUserName, resContent)
    return responseDict
