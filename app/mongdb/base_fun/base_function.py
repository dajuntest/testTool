#coding=utf-8
import pymongo


class BaseMongoFun(object):

    def __init__(self, db='testdata'):  # , db_url='localhost:27017', user='dajun', password='dajun'
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = myclient[db]


    def insert_one(self, collection, data):
        # mydict = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}
        # {"_id": 1, "name": "RUNOOB", "cn_name": "菜鸟教程"}
        mycol = self.mydb[collection]
        mycol.insert_one(data)

    def insert_many(self, collection, data):
        # mylist = [
        #     {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
        #     {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
        #     {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
        #     {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
        #     {"name": "Github", "alexa": "109", "url": "https://www.github.com"}
        # ]
        mycol = self.mydb[collection]
        mycol.insert_many(data)

    def find_one(self, collection):
        mycol = self.mydb[collection]
        print(mycol.find_one())

    def find_all(self, collection):
        mycol = self.mydb[collection]
        for x in mycol.find():
            print(x)

# if __name__ == '__main__':
#     mydict = {"name": "Google", "alexa": "1", "url": "https://www.google.com"}
#     BaseMongoFun().insert_one('cpc_account', mydict)