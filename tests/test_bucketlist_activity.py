import unittest

from bucketlist import app, models

class BucketlistActivitySmartGoalsTestCase(unittest.TestCase):
    def setUp(self):
        self.tester = app.test_client(self)
        self.user1 = models.User()
        self.user1_bucketlist = models.Bucketlist()
        self.user1_bucketlist_activity = models.Bucketlist_Activities()

        models.all_users = {} #master user list
        models.all_bucketlists = {} #master bucketlist list
        models.all_bucketlists_activities = {} #master bucketlist activity

    def test_user_can_create_bucketlist_activity(self):
        self.user1.create_user("Zach Reed", "zreed@email.com", "qaz12#@")

        self.user1_bucketlist.create_bucketlist(models.all_users['zreed@email.com'][1],
                                                'Career Things',
                                                'Goals to achieve in my career')

        self.user1_bucketlist_activity.create_bucketlist_activity(
            models.all_users['zreed@email.com'][1],
            'Career Things',
            'Achieve A', '01/01/2018', False)

        self.assertEqual(models.all_bucketlists_activities
                         [models.all_users['zreed@email.com'][1]][0],
                         {'Career Things':'01/01/2018', 'Achieve A':False},
                         "User cannot create bucketlist activity")

    def test_user_can_create_more_than_one_bucketlist_activity(self):
        self.user1.create_user("Zach Reed", "zreed@email.com", "qaz12#@")

        self.user1_bucketlist.create_bucketlist(models.all_users['zreed@email.com'][1],
                                                'Career Things',
                                                'Goals to achieve in my career')

        self.user1_bucketlist_activity.create_bucketlist_activity(
            models.all_users['zreed@email.com'][1],
            'Career Things',
            'Achieve A', '01/01/2018', False)

        self.user1_bucketlist_activity.create_bucketlist_activity(
            models.all_users['zreed@email.com'][1],
            'Career Things',
            'Achieve XYZ', '01/01/2018', False)

        count = len(models.all_bucketlists_activities['zreed@email.com'])

        self.assertEqual(count, 2, "User cannot create multiple bucketlist activities")

    def test_user_can_update_bucketlist_activity(self):
        self.user1.create_user("Zach Reed", "zreed@email.com", "qaz12#@")

        self.user1_bucketlist.create_bucketlist(models.all_users['zreed@email.com'][1],
                                                'Career Things',
                                                'Goals to achieve in my career')

        self.user1_bucketlist_activity.create_bucketlist_activity(
            models.all_users['zreed@email.com'][1],
            'Career Things',
            'Achieve A', '01/01/2018', False)

        self.user1_bucketlist_activity.create_bucketlist_activity(
            models.all_users['zreed@email.com'][1],
            'Career Things',
            'Achieve XYZ', '01/01/2018', False)

        self.user1_bucketlist_activity.update_bucketlist_activity(
            models.all_users['zreed@email.com'][1], 0, 'Career Things', '01/02/2018',
            'Achieve Promotion', False)


        compare_list = []
        compare = False
        for key, value in models.all_bucketlists_activities\
                                 [models.all_users['zreed@email.com'][1]][0].items():
            compare_list.append(key)
            compare_list.append(value)


        if 'Achieve Promotion' in compare_list\
                               and '01/02/2018' in compare_list\
                               and 'Career Things' in  compare_list:
            compare = True



        self.assertEqual(compare, True, "User cannot update bucketlist")



    def test_user_cannot_make_bucketlist_activity_without_bucketlist(self):
        self.user1.create_user("Jane Zeed", "jzeed@email.com", "qaz12#@")

        self.user1_bucketlist.create_bucketlist(models.all_users['jzeed@email.com'][1],
                                                'Career Things',
                                                'Goals to achieve in my career')

        self.user1_bucketlist_activity.create_bucketlist_activity(
            models.all_users['jzeed@email.com'][1],
            'Career Things',
            'Achieve Milestone', '01/01/2018', False)

        self.user1_bucketlist_activity.create_bucketlist_activity(
            models.all_users['jzeed@email.com'][1],
            'Career Things',
            'Achieve Promotion', '05/06/2018', False)

        self.user1_bucketlist_activity.delete_bucketlist_activity(
            models.all_users['jzeed@email.com'][1], 1)

        count = len(models.all_bucketlists_activities['jzeed@email.com'])

        self.assertEqual(count, 1, "User cannot delete bucketlist activities")
