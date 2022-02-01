from Commons.MyMongo import GetMongodb
from pymongo import DESCENDING, ASCENDING
import json

collectionName = "myBlog"


def GetCollection(MongoHost, MongoPwd):
    return GetMongodb(MongoHost, MongoPwd).get_collection(collectionName)


def removeBlogListContents(blogOne):
    blogOne.pop('_id')
    return blogOne


def GetBlogListInfo(MongoHost, MongoPwd, perPage: int):
    collection = GetCollection(MongoHost, MongoPwd)
    # 总页数查询
    count = collection.estimated_document_count()
    totalPage = int(count / perPage) + 1 if count % perPage > 0 else int(count / perPage)
    return count, totalPage


def GetBlogListByPage(MongoHost, MongoPwd, page: int, perPage: int, queryStr=None, sortItemKey=None, sortOrder=None):
    collection = GetCollection(MongoHost, MongoPwd)
    finderDic = json.loads(queryStr) if queryStr is not None else None
    sortKey = "blogID" if sortItemKey is None else sortItemKey
    sortOrderMongo = ASCENDING if sortOrder is None else DESCENDING
    # 分页查询
    blogListCursor = collection.find(finderDic). \
        sort([(sortKey, sortOrderMongo)]).skip(perPage * (page - 1)).limit(perPage) \
        if finderDic is not None \
        else collection.find(). \
        sort([(sortKey, sortOrderMongo)]).skip(perPage * (page - 1)).limit(perPage)
    return list(filter(lambda blogOne: blogOne.pop('_id'), blogListCursor))
