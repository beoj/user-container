from django.test import TestCase
from user.core import mongo

from user.core import models

class User(TestCase):
    def setUp(self):
        mongo.userTable.insert_one({
            "displayName": "namprozz",
            "realName": "Nguyen Van Nam",
            "email": "namnguyenvan@gmai.com",
            "password": "namdeptrai",
            "introduction": "Toi rat dep trai",
            "avatar": "",
            "dateSignup": 1586210447,
            "banStatus": False,
            "report": [],
            "comment": [],
            "problemAccepted": [],
            "submission": [],
            "contestJoin": [],
            "point": 123,
            "blog": [],
            "contestPoint": 45,
            "contestArmorial": ["silver"],
            "session": [],
        })
        mongo.userTable.insert_one({
            "displayName": "vietthongminh",
            "realName": "Ly Thuong Viet",
            "email": "vietthongminh@abc.com",
            "password": "234ssdwfF",
            "introduction": "Toi rat thong minh",
            "avatar": "",
            "dateSignup": 1672842376,
            "banStatus": False,
            "report": [],
            "comment": [],
            "problemAccepted": [],
            "submission": [],
            "contestJoin": [],
            "point": 65,
            "blog": [],
            "contestPoint": 100,
            "contestArmorial": ["gold"],
            "session": [],
        })
        mongo.userTable.insert_one({
            "displayName": "toward",
            "realName": "Toward Linus",
            "email": "towardlinus@linux.com",
            "password": "123dffg8098",
            "introduction": "Hello everyone",
            "avatar": "",
            "dateSignup": 1620048894,
            "banStatus": False,
            "report": [],
            "comment": [],
            "problemAccepted": [],
            "submission": [],
            "contestJoin": [],
            "point": 41,
            "blog": [],
            "contestPoint": 10,
            "contestArmorial": ["gold"],
            "session": [],
        })
        mongo.userTable.insert_one({
            "displayName": "ricardo",
            "realName": "Ricardo Gray",
            "email": "ricardothehow@outlook.com",
            "password": "123456",
            "introduction": "I'm a software developer",
            "avatar": "",
            "dateSignup": 1594188304,
            "banStatus": True,
            "report": [],
            "comment": [],
            "problemAccepted": [],
            "submission": [],
            "contestJoin": [],
            "point": 54,
            "blog": [],
            "contestPoint": 12,
            "contestArmorial": [],
            "session": [],
        })
        mongo.userTable.insert_one({
            "displayName": "billy",
            "realName": "Bill Gates",
            "email": "billgates@microsoft.com",
            "password": "534dvvbnBdfgiwe7u8",
            "introduction": "I hate programming",
            "avatar": "",
            "dateSignup": 1610183104,
            "banStatus": False,
            "report": [],
            "comment": [],
            "problemAccepted": [],
            "submission": [],
            "contestJoin": [],
            "point": 1254,
            "blog": [],
            "contestPoint": 0,
            "contestArmorial": [],
            "session": [],
        })
        mongo.userTable.insert_one({
            "displayName": "hieupc",
            "realName": "Dang Van Hieu",
            "email": "hieupc@gmail.com",
            "password": "asdfw4etg093458df",
            "introduction": "Hello",
            "avatar": "",
            "dateSignup": 1675382706,
            "banStatus": False,
            "report": [],
            "comment": [],
            "problemAccepted": [],
            "submission": [],
            "contestJoin": [],
            "point": 1,
            "blog": [],
            "contestPoint": 27,
            "contestArmorial": ["copper"],
            "session": [],
        })
        mongo.userTable.insert_one({
            "displayName": "nguyentai",
            "realName": "La Nguyen Tai",
            "email": "taichanh@gmail.com",
            "password": "fasdf21fha",
            "introduction": "I love Dijkstra",
            "avatar": "",
            "dateSignup": 1675382706,
            "banStatus": True,
            "report": [],
            "comment": [],
            "problemAccepted": [],
            "submission": [],
            "contestJoin": [],
            "point": 3456,
            "blog": [],
            "contestPoint": 999,
            "contestArmorial": ["diamond"],
            "session": [],
        })
    
    def tearDown(self):
        return mongo.userTable.delete_many({})
    
    def testPickOneFromDatabase_1(self):
        user = models.User.oneFromDatabase({"displayName": "namprozz"})
        self.assertEqual(user.email, "namnguyenvan@gmai.com")

    def testPickOneFromDatabase_2(self):
        user = models.User.oneFromDatabase({"displayName": "vietthongminh"})
        self.assertEqual(user.email, "vietthongminh@abc.com")

    def testPickOneFromDatabase_3(self):
        user = models.User.oneFromDatabase({"displayName": "hieupc"})
        self.assertEqual(user.email, "hieupc@gmail.com")

    def testPickOneFromDatabase_4(self):
        user = models.User.oneFromDatabase({"displayName": "nguyentai"})
        self.assertEqual(user.email, "taichanh@gmail.com")

    def testPickManyFromDatabase_1(self):
        arrUser = list(models.User.manyFromDatabase({"contestArmorial": "gold"}))
        self.assertEqual(len(arrUser), 2)

    def testPickManyFromDatabase_2(self):
        arrUser = list(models.User.manyFromDatabase({"banStatus": False}))
        self.assertEqual(len(arrUser), 5)

    def testPickManyFromDatabase_3(self):
        arrUser = list(models.User.manyFromDatabase({"banStatus": True}))
        self.assertEqual(len(arrUser), 2)

    def testUpdateUser_1(self):
        user = models.User.oneFromDatabase({"displayName": "namprozz"})
        user.introduction = "Hello everyone"
        user.updateToDatabase()

        user = models.User.oneFromDatabase({"displayName": "namprozz"})
        self.assertEqual(user.introduction, "Hello everyone")

    def testUpdateUser_2(self):
        user = models.User.oneFromDatabase({"email": "taichanh@gmail.com"})
        user.banStatus = False
        user.updateToDatabase()

        user = models.User.oneFromDatabase({"email": "taichanh@gmail.com"})
        self.assertEqual(user.banStatus, False)

    def testUpdateUser_3(self):
        user = models.User.oneFromDatabase({"displayName": "ricardo"})
        user.point = 100
        user.updateToDatabase()

        user = models.User.oneFromDatabase({"displayName": "ricardo"})
        self.assertEqual(user.point, 100)

    def testAddUser_1(self):
        user = models.User.oneFromDict({
            "displayName": "abc",
            "realName": "Nguyen Van A",
            "email": "a@a.com",
            "password": "asdf5wertS!",
            "introduction": "A",
            "dateSignup": 1586685614,
            "banStatus": False,
        })
        user.updateToDatabase()

        user = models.User.oneFromDatabase({"displayName": "abc"})
        self.assertEqual(user.email, "a@a.com")

    def testAddUser_2(self):
        user = models.User.oneFromDict({
            "displayName": "cdef",
            "realName": "Nguyen Thi B",
            "email": "b@google.com",
            "password": "56784esd@1r",
            "introduction": "BBNBBB",
            "dateSignup": 1618648981,
        })
        user.updateToDatabase()

        user = models.User.oneFromDatabase({"email": "b@google.com"})
        self.assertEqual(user.displayName, "cdef")

    def testAddUser_3(self):
        user = models.User.oneFromDict({
            "displayName": "asdf",
            "realName": "Dang Van Asdf",
            "email": "asdf@asdf.com",
            "password": "123456",
            "introduction": "asdf",
            "dateSignup": 1682203394,
        })
        user.updateToDatabase()

        user = models.User.oneFromDatabase({"email": "asdf@asdf.com"})
        self.assertEqual(user.realName, "Dang Van Asdf")

    def testDeleteUser_1(self):
        user = models.User.oneFromDatabase({"displayName": "namprozz"})
        user.deleteFromDatabase()

        user = list(models.User.manyFromDatabase({"displayName": "namprozz"}))
        self.assertEqual(bool(user), False)

    def testDeleteUser_2(self):
        user = models.User.oneFromDatabase({"email": "towardlinus@linux.com"})
        user.deleteFromDatabase()

        user = list(models.User.manyFromDatabase({"email": "towardlinus@linux.com"}))
        self.assertEqual(bool(user), False)

    def testDeleteUser_3(self):
        user = models.User.oneFromDatabase({"dateSignup": 1610183104})
        user.deleteFromDatabase()

        user = list(models.User.manyFromDatabase({"dateSignup": 1610183104}))
        self.assertEqual(bool(user), False)