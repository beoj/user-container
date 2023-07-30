'''
Class cho việc xử lí dữ liệu từ database
'''

from . import mongo

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
                 banStatus,
                 dateSignup,
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
                 contestArmorial = []
                 ):
        self._id = _id
        self.displayName = displayName
        self.realName = realName
        self.email = email
        self.password = password
        self.introduction = introduction
        self.avatar = avatar
        self.dateSignup = dateSignup
        self.banStatus = banStatus
        self.report = report
        self.comment = comment
        self.problemAccepted = problemAccepted
        self.submission = submission
        self.contestJoin = contestJoin
        self.point = point
        self.blog = blog
        self.contestPoint = contestPoint
        self.contestArmorial = contestArmorial
    
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