import unittest
import sys, hashlib
from bucketlist import app, models, views
from flask import request

class UserSmartGoalsTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
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
    
    def test_user_can_register(self):

        response = self.tester.post('/sign-up/new-user',
                                    data=dict(fullname="James Brown",
                                              email="jb@email.com",
                                              password="ABC",
                                              confirm_password="ABC"),
                                    follow_redirects=True)

        assert b"Smart Goals | Login" in response.data

    def test_registered_user_can_login(self):
        self.user1.create_user("James Brown", "jb@email.com", "ABC")

        response1 = self.tester.post('/sign-up/new-user',
                                     data=dict(fullname="James Brown",
                                               email="jb@email.com",
                                               password="ABC",
                                               confirm_password="ABC"),
                                     follow_redirects=True)

        assert b"Smart Goals | Login" in response1.data

        response2 = self.tester.post('/auth/',
                                     data=dict(email="jb@email.com",
                                               password="ABC"),
                                     follow_redirects=True)

        # User has logged in
        self.assertIn("jb@email.com", models.all_users)
        assert b"Hello James Brown" in response2.data

    def test_invalid_user_cannot_login(self):
        response = self.tester.post('/auth/', data=dict(email="somename@email.com",
                                                        password="ABC"),
                                    follow_redirects=True)

        assert b"Invalid Credentials!" in response.data

    def test_user_entered_invalid_password(self):
        self.user1.create_user("James Brown", "jb@email.com", "ABC")

        response = self.tester.post('/auth/',
                                    data=dict(email="jb@email.com", password="notpassword"))

        assert b"Invalid Credentials!" in response.data



    def test_login_form_appears_if_form_not_valid(self):
        app.config['WTF_CSRF_ENABLED'] = True
        self.user1.create_user("James Brown", "jb@email.com", "ABC")
        response = self.tester.post('/auth/',
                                    data=dict(email="lj@email.com",
                                              password="ABCz"),
                                    follow_redirects=True)

        assert b"Smart Goals | Login" in response.data

    def test_current_user_can_be_set(self):
        user_details = ["James Brown",
                        "jb@email.com", "3c01bdbb26f358bab27f267924aa2c9a03fcfdb8"]

        views.set_current_user(user_details)
        self.assertEqual(views.current_user,
                         ["James Brown",
                          "jb@email.com", "3c01bdbb26f358bab27f267924aa2c9a03fcfdb8"],
                         "Current user variable cannot be set")

    def test_check_when_no_current_user(self):
        user_details = []

        views.set_current_user(user_details)
        self.assertEqual(views.current_user, [], "Current User cannot be set to empty list")


