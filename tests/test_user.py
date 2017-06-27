import unittest

from bucketlist import app, models

class UserSmartGoalsTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        self.user1 = models.User()
        models.all_users = {}

    ## Test if User object can be created/ Sign Up
    def test_user_class_can_be_instantiated(self):

        self.user1.create_user("James Brown", "jb@email.com", "ABC")
        self.assertIsInstance(models.all_users["jb@email.com"], list,
                              "Master User list is not created")

    def test_more_than_one_user(self):
        self.user1.create_user("James Brown", "jb@email.com", "ABC")
        self.user2 = models.User()
        self.user2.create_user("Fred Oroo", "foroo@email.com", "XYZ")

        count = len(models.all_users)
        self.assertEqual(count, 2, "Cannot create more than 1 user")
    