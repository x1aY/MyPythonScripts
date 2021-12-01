import re
import requests
from functools import reduce
from bs4 import BeautifulSoup
from Commons.MyMongo import GetMongodb
from Commons.MyParsePdf import OnlinePdf2TextList

baseUrl = 'https://cies.hhu.edu.cn/'
lecPage = "_s97/4118/list.psp"
myCollection = None
collectionName = 'autoExtractLec'

def GetSoup(url=baseUrl):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def GetOldLecs(MongoHost, MongoPwd, collection):
    if collection is None:
        collection = GetMongodb(MongoHost, MongoPwd).get_collection(collectionName)
    res = collection.find_one()
    assert res is not None
    return res.get('oldLecNum'), res.get('old5Lecs')


def UpdateMongodb(collection, oldLecNum, newLecNum, new5Lecs):
    if collection is not None:
        collection.update({'oldLecNum': oldLecNum}, {'oldLecNum': newLecNum, 'old5Lecs': new5Lecs})


def GetNewLecture(soup, oldLecNum,
                  numEle='em', numClass="all_count", pattern="^学术报告.*$", linkBase='https://cies.hhu.edu.cn'):
    currLecNum = int(soup.find(name=numEle, attrs={"class": numClass}).text)
    alllink = soup.find_all(name='a', attrs={"title": re.compile(pattern)})
    first5Lecs = [{"title": linkOne['title'], "href": linkBase + linkOne['href']} for linkOne in alllink][:5]
    firstLec = first5Lecs[0]
    hasNewLec = True if currLecNum > oldLecNum else False
    return first5Lecs, hasNewLec, firstLec


def GetLecPdfLink(soup, pdflinkEle='div', pdfLinkClass='wp_pdf_player', pdfLinkSrcName='pdfsrc'):
    return baseUrl + soup.find_all(name=pdflinkEle, attrs={'class': pdfLinkClass})[0][pdfLinkSrcName]


def PdfLink2LecStr(url, pdfBriefHeader="摘要"):
    lectureTexts = OnlinePdf2TextList(url)
    absIndex = lectureTexts.index(
        list(filter(lambda text: pdfBriefHeader in text, lectureTexts))[0])
    lectureStr = reduce(lambda text1, text2: text1 + text2, lectureTexts[:absIndex])
    return re.sub(' +', ' ', lectureStr)


def AutoExtractLec(MongoHost, MongoPwd):
    oldLecNum, old5Lecs = GetOldLecs(MongoHost, MongoPwd, myCollection)
    first5Lecs, hasNewLec, firstLec = GetNewLecture(GetSoup(baseUrl + lecPage), oldLecNum)
    newLecStr = PdfLink2LecStr(GetLecPdfLink(GetSoup(firstLec.get('href'))))
    return newLecStr
    # return oldLecNum,old5Lecs,first5Lecs,hasNewLec,firstLec
    # if hasNewLec:
    #     UpdateMongodb(myCollection,oldLecNum,oldLecNum+1,first5Lecs)


if __name__ == '__main__':
    print('in AutoExtractLecture')
