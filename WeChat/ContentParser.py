from operator import methodcaller


def ParseByMsgType(msgType, content, xmlDict):
    return methodcaller(MyParser.funcDict.get(msgType), content, xmlDict)(MyParser)


class MyParser:
    funcDict = {'text': 'ParseText'}

    @staticmethod
    def ParseText(text, xmlDict):
        return text
