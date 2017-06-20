import unittest

from bucketlist import app, models

class SmartGoalsTestCase(unittest.TestCase):

    #test if pages return 200 Ok message when called
    def test_index_page_works(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    
    def test_login_page_works(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    

    def test_signup_page_works(self):
        tester = app.test_client(self)
        response = tester.get('/sign-up', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_about_page_works(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_contact_page_works(self):
        tester = app.test_client(self)
        response = tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_missing_templates_status(self):
        #Testing status code response page not found"""
        tester = app.test_client(self)
        response = tester.get('/xyz-page', content_type='html/text')
        self.assertEqual(response.status_code, 404)

    def test_custom_message_for_page_not_found(self):
        tester = app.test_client(self)
        response = tester.get('/xyz-page', content_type='html/text')
        self.assertTrue(b'Page Not' in response.data, msg="Custom 404 page not working")

    ## Test if User object can be created
    def test_user_class_can_be_instantiated(self):
        user1 = models.User("James Brown", "jb@email.com", "ABC")
        self.assertEqual(user1.getUser(), {"James Brown", "jb@email.com", "3c01bdbb26f358bab27f267924aa2c9a03fcfdb8"}, 
                         "User not created")





if __name__ == "__main__":
    unittest.main()


