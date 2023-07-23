from django.test import TestCase

class ClientAccessUser(TestCase):
    def test_user_page_status(self):
        response = self.client.get('/user/')
        self.assertEqual(response.status_code, 200)