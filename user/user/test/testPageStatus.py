from django.test import TestCase

class user(TestCase):
    def testResponse(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)
