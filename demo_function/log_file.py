#!/usr/bin/python3

import pymongo

# db_url = 'localhost:27017'
# db = 'testdata'
# user = 'dajun'
# password = 'dajun'
#
# url = "mongodb://" + user + ':' + password + '@' + db_url + '/'
# print(url)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["testdata"]
mycol = mydb["cpc_account"]



mydict = {"name": "RUNOOB", "alexa": "10000", "url": "https://www.runoob.com"}

x = mycol.insert_one(mydict)
print(x)


#
# def __init__(self, db_url='localhost:27017', db='testdata', user='dajun', password='dajun'):
#     myclient = pymongo.MongoClient("mongodb://" + user + ':' + password + '@' + db_url)
#     self.mydb = myclient[db]