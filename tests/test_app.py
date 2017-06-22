import unittest

from bucketlist import app, models

class SmartGoalsTestCase(unittest.TestCase):

    def setUp(self):
        self.tester = app.test_client(self)

    #test if pages return 200 Ok message when called
    def test_index_page_works(self):

        response = self.tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_login_page_works(self):
        response = self.tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_signup_page_works(self):
        response = self.tester.get('/sign-up', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_about_page_works(self):
        response = self.tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_contact_page_works(self):
        response = self.tester.get('/contact', content_type='html/text')
        self.assertEqual(response.status_code, 200)


    def test_missing_templates_status(self):
        #Testing status code response page not found"""
        response = self.tester.get('/xyz-page', content_type='html/text')
        self.assertEqual(response.status_code, 404)


    def test_custom_message_for_page_not_found(self):
        response = self.tester.get('/xyz-page', content_type='html/text')
        self.assertTrue(b'Page Not' in response.data, msg="Custom 404 page not working")


    ## Test if User object can be created/ Sign Up
    def test_user_class_can_be_instantiated(self):
        user1 = models.User("James Brown", "jb@email.com", "ABC")
        self.assertEqual(user1.getUser(), {"name":"James Brown", "email":"jb@email.com",
                                           "password":"3c01bdbb26f358bab27f267924aa2c9a03fcfdb8"},
                         "User not created")


    # Test to check if User can update their details
    def test_user_can_update_details(self):
        user1 = models.User("James Brown", "jamesbr@gmail.com", "ABC")
        self.assertEqual(user1.updateUser("James Brown", "jamesbrown@gmail.com"),
                         {"name":"James Brown", "email":"jamesbrown@gmail.com",
                          "password":"3c01bdbb26f358bab27f267924aa2c9a03fcfdb8"},
                         "User details cannot be updated")


    def test_user_enters_blank_details(self):
        user1 = models.User("", "", "")
        self.assertEqual(user1.getUser(), {"name":'', "email":'',
                                           "password":'da39a3ee5e6b4b0d3255bfef95601890afd80709'},
                         "User Should not be allowed blank form submission")


    def test_user_email_is_correct_format(self):
        user2 = models.User("Lucy Deeds", "lucydeeds@gmail.com", "ABC")
        self.assertTrue('@' in user2.email, "User email is not correct")


    # Bucket list test cases
    def test_user_can_create_bucketlist(self):
        user1_bucketlist = models.Bucketlist()
        user1_bucketlist.clear_bucketlist()
        user1_bucketlist.create_bucketlist('Career Things', 'Goals to achieve in my career')
        self.assertEqual(user1_bucketlist.get_bucketlists(),
                         [{"Career Things":"Goals to achieve in my career"}],
                         "Cannot create bucketlist")


    def test_bucketlist_returns_list(self):
        user2_bucketlist = models.Bucketlist()
        user2_bucketlist.clear_bucketlist()
        user2_bucketlist.create_bucketlist("Traveling", "Places to visit")
        self.assertIsInstance(user2_bucketlist.get_bucketlists(),
                              list,
                              "Bucketlist does not return a list")


    def test_bucketlist_activity_is_of_bucketlist_class(self):

        self.assertEqual(issubclass(models.Bucketlist_Activities, models.Bucketlist), True,
                         "bucketlist activity is not an instance of bucketlist")


    def test_user_can_update_bucketlist(self):
        user4_bucketlist = models.Bucketlist()
        user4_bucketlist.clear_bucketlist()
        user4_bucketlist.create_bucketlist('Movie Watch', 'Must Watch these')
        user4_bucketlist.update_bucketlist(0, 'Movie to Watch', 'Must Watch these')
        self.assertEqual(user4_bucketlist.get_bucketlists(),
                         [{'Movie to Watch': 'Must Watch these'}],
                         "Cannot create bucketlist")


    def test_user_can_make_more_than_one_bucketlist(self):
        user5_bucketlist = models.Bucketlist()
        user5_bucketlist.create_bucketlist('Movie Watch', 'Must Watch these')
        user5_bucketlist.create_bucketlist('Attend 5 Live events', 'Site A, has all sites')

        count = len(user5_bucketlist.get_bucketlists())

        self.assertEqual(count, 2, "Cannot create more than 1 bucketlist")


    def test_user_can_remove_one_bucketlist_when_two(self):
        user6_bucketlist = models.Bucketlist()
        user6_bucketlist.clear_bucketlist()
        user6_bucketlist.create_bucketlist('Must drive cars', 'Cars I must drive')
        user6_bucketlist.create_bucketlist('Adrenaline stunts',
                                           'Things to make the adrenaline rush')

        count = len(user6_bucketlist.delete_bucketlist(0))

        self.assertEqual(count, 1, "Cannot remove bucketlist items")


    def test_user_can_create_bucketlist_activity(self):
        user7_bucketlist = models.Bucketlist()
        user7_bucketlist.clear_bucketlist()
        user7_bucketlist.create_bucketlist('Career Things', 'Career milestones')

        bucketlist_activity = models.Bucketlist_Activities()
        bucketlist_activity.clear_bucketlist_activity()
        bucketlist_activity.create_bucketlist_activity('Career Things', 'Achieve A',
                                                       '01/01/2018', False)

        self.assertEqual(bucketlist_activity.get_bucketlist_ativities(),
                         [{'Achieve A':False}], "User cannot create a bucketlist")

        self.assertEqual(bucketlist_activity.get_bucketlists_activity_detail('Achieve A'),
                         {'Career Things':'01/01/2018'},
                         "User does not have activity details")


    def test_user_can_update_bucketlist_activity(self):
        user8_bucketlist = models.Bucketlist()
        user8_bucketlist.clear_bucketlist()
        user8_bucketlist.create_bucketlist('Career Things', 'Career milestones')

        bucketlist_activity = models.Bucketlist_Activities()
        bucketlist_activity.clear_bucketlist_activity()
        bucketlist_activity.create_bucketlist_activity('Career Things', 'Achieve A',
                                                       '01/01/2018', False)


        bucketlist_activity.update_bucketlist_activity(0, 'Career Things',
                                                       'Achieve promotion',
                                                       '01/02/2018', False)

        self.assertEqual(bucketlist_activity.get_bucketlist_ativities()[0],
                         {'Achieve promotion':False})

    def test_user_can_remove_bucketlist_activity(self):
        user9_bucketlist = models.Bucketlist()
        user9_bucketlist.clear_bucketlist()
        user9_bucketlist.create_bucketlist('Travel things', 'Places to travel')

        bucketlist_activity = models.Bucketlist_Activities()
        bucketlist_activity.clear_bucketlist_activity()
        bucketlist_activity.create_bucketlist_activity('Travel Things', 'Travel to Z',
                                                       '01/01/2018', False)

        bucketlist_activity.create_bucketlist_activity('Travel things', 'Travel to B',
                                                       '01/02/2018', False)

        count = len(bucketlist_activity.delete_bucketlist_activity(0))

        self.assertEqual(count, 1, "Cannot delete bucketlist activity")



if __name__ == "__main__":
    unittest.main()
