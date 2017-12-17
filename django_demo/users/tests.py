from rest_framework.test import APITestCase
from constance import config


class UserTestCase(APITestCase):
    def test(self):
        self.assertTrue(True)

    def test_user(self):
        self.assertTrue(True)
        print(config.THE_ANSWER)
