from test_plus.test import TestCase

class LoggedUser(TestCase):
    def setUp(self):
        self.user = self.make_user('client')
        self.client.force_login(user=self.user)