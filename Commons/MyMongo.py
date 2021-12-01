from pymongo import MongoClient


def GetMongodb(host, pwd, user='root', db='scripts', port=27017):
    client = MongoClient(host=host, port=port, connect=False, username=user, password=pwd)
    return client.get_database(db)
