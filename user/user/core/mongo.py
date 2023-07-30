'''
Xử lý kết nối đến MongoDB
'''

import pymongo
from bson.objectid import ObjectId
import os

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')

USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')

clientMongo = pymongo.MongoClient(f'mongodb://{USER}:{PASSWORD}@{HOST}:{PORT}/')

userTable = clientMongo['beoj']['user']