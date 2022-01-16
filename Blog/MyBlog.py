from Commons.MyMongo import GetMongodb
from pymongo import DESCENDING, ASCENDING
import json

collectionName = "myBlog"


def GetBlogListByPage(MongoHost, MongoPwd, page: int, perPage: int, queryStr=None, sortItemKey=None, sortOrder=None):
    collection = GetMongodb(MongoHost, MongoPwd).get_collection(collectionName)
    finderDic = json.loads(queryStr) if queryStr is not None else None
    sortKey = "blogId" if sortItemKey is None else sortItemKey
    sortOrderMongo = DESCENDING if sortOrder is None else ASCENDING
    # 总页数查询
    count = len(list(collection.find(finderDic))) \
        if finderDic is not None \
        else len(list(collection.find()))
    totalPage = int(count / perPage) + 1 if count % perPage > 0 else int(count / perPage)
    # 分页查询
    blogListCursor = collection.find(finderDic).sort([(sortKey, sortOrderMongo)]).skip(perPage * (page - 1)).limit(
        perPage) \
        if finderDic is not None \
        else collection.find().sort([(sortKey, sortOrderMongo)]).skip(perPage * (page - 1)).limit(perPage)
    blogList = list(filter(lambda blogListOne: blogListOne.pop('_id'), blogListCursor))
    return totalPage, blogList
