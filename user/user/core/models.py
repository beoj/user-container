'''
Class cho việc xử lí dữ liệu từ database
'''

import time
import random

from . import mongo

def getClientIP(request):
    '''
    Lấy IP của client

    Trả về IP của client dạng string
    '''

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def generateKeySession():
    '''
    Tạo ra key ngẫu nhiên dài 64 kí tự

    Trả về key dạng string
    '''

    charArr = '!#%&()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[]^_`abcdefghijklmnopqrstuvwxyz|'
    key = ''
    for i in range(64):
        key += random.choice(charArr)

    return key

class User:
    '''
    Class xử lí dữ liệu User
    '''
    def __init__(self,
                 _id,
                 displayName,
                 realName,
                 email,
                 password,
                 dateSignup,
                 banStatus = False,
                 introduction = '',
                 avatar = '',
                 report = [],
                 comment = [],
                 problemAccepted = [],
                 submission = [],
                 contestJoin = [],
                 point = 0,
                 blog = [],
                 contestPoint = 0,
                 contestArmorial = [],
                 session = []
                 ):
        self._id = _id
        self.displayName = str(displayName)
        self.realName = str(realName)
        self.email = str(email)
        self.password = str(password)
        self.introduction = str(introduction)
        self.avatar = avatar
        self.dateSignup = int(dateSignup)
        self.banStatus = bool(banStatus)
        self.report = list(report)
        self.comment = list(comment)
        self.problemAccepted = list(problemAccepted)
        self.submission = list(submission)
        self.contestJoin = list(contestJoin)
        self.point = int(point)
        self.blog = list(blog)
        self.contestPoint = int(contestPoint)
        self.contestArmorial = list(contestArmorial)
        self.session = list(session)
    
    def updateToDatabase(self):
        '''
        Nếu Object đã có trong database thì update
        Nếu Object chưa có trong database thì insert

        Không trả về giá trị
        '''

        if bool(list(mongo.userTable.find({'_id': self._id}))):
            mongo.userTable.update_one({'_id': self._id}, {'$set': self.__dict__})
        else:
            mongo.userTable.insert_one(self.__dict__)

    def deleteFromDatabase(self):
        '''
        Xóa Oject trong Database

        Không trả về giá trị
        '''
        
        mongo.userTable.delete_one({'_id': self._id})

    def createSession(self, request, response):
        '''
        Tạo ra một session đăng nhập cho client sau đó tự update vào Database
        Thêm vào cookie của client giá trị key
        Mỗi session có thời hạn 1 tháng

        Trả về key của session dạng string
        '''

        session = {
            "ip":   getClientIP(request),
            "dateCreate": round(time.time()),
            "key":  generateKeySession(),
        }

        self.session.append(session)
        response.set_cookie('key', session["key"])

        self.updateToDatabase()
        return session["key"]
    
    def deleteSession(self, key):
        '''
        Xóa session bằng key của session đó
        Sau khi xóa thì tự update vào Database

        Không trả về giá trị
        '''
        
        for i in self.session:
            if i['key'] == key:
                self.session.remove(i)
                break
        self.updateToDatabase()

    @classmethod
    def oneFromDatabase(cls, dictFind):
        '''
        Dữ liệu lấy từ Database
        Lấy user đầu tiên tìm được bằng hàm find của pymongo với giá trị dictFind

        Trả về một object từ class User
        '''

        firstUser = dict(mongo.userTable.find(dictFind)[0])
        return cls(**firstUser)

    @classmethod
    def oneFromCookie(cls, request):
        '''
        Dữ liệu lấy từ Database
        Dùng session key để lấy user mà session đó đang đăng nhập

        Nếu session đã hết hạn thì trả về lỗi Exception("The session is expired")
        Trả về một object từ class User
        '''

        key = request.COOKIES['key']
        user = cls.oneFromDatabase({'session.key': key})
        for i in user.session:
            if i['key'] == key:
                if i['dateCreate'] + 2592000 < time.time(): # 1 tháng = 30 ngày = 2592000 giây
                    raise Exception("The session is expired")
                elif i['ip'] != getClientIP(request):
                    raise Exception("The request ip do not match the session ip")
                return user

    @classmethod
    def manyFromDatabase(cls, dictFind):
        '''
        Dữ liệu lấy từ Database
        Lấy tất cả user tìm được bằng hàm find của pymongo với giá trị dictFind

        Trả về một list những object từ class User
        '''

        for user in mongo.userTable.find(dictFind):
            yield cls(**dict(user))

    @classmethod
    def oneFromDict(cls, dictInput):
        '''
        Dữ liệu lấy từ một dict
        Tạo một user mới từ dictInput

        Trả về một object từ class User
        '''

        # Thêm _id vào dictInput
        _id = mongo.ObjectId()
        while bool(list(mongo.userTable.find({'_id': _id}))):
            _id = mongo.ObjectId()
        dictInput.update({'_id': _id})
        del _id

        return cls(**dictInput)