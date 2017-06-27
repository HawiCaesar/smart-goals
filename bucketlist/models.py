# -*- coding: utf-8 -*-
import hashlib # Used for hashing
all_users = {}
all_bucketlists = {}
all_bucketlists_activities = {}

class User(object):
    # User created when __init__ runs

    def create_user(self, full_name, email, password):
        self.fullname = full_name
        self.email = email

        # make password into hash
        hash_object = hashlib.sha1(password.encode())
        self.password = hash_object.hexdigest()

        all_users[self.email] = [self.fullname, self.email, self.password]


class Bucketlist(object):

    bucketlist = {}

    def create_bucketlist(self, current_user, bucketlist_name, bucketlist_description):
        """ Create a bucketlist and append it to the master bucketlist"""

        self.bucketlist = {bucketlist_name:bucketlist_description}

        if current_user in all_bucketlists:
            all_bucketlists[current_user].append(self.bucketlist)

        else:
            all_bucketlists[current_user] = [self.bucketlist]


    def update_bucketlist(self, current_user, bucketlist_key,
                          new_bucketlist_name, new_bucketlist_description):

        """ get the bucket list key and update the new details of the bucketlist """

        user_bucketlists = all_bucketlists[current_user]

        update_bucketlist = user_bucketlists[bucketlist_key]

        update_bucketlist = {new_bucketlist_name:new_bucketlist_description}

        all_bucketlists[current_user][bucketlist_key] = update_bucketlist



    def delete_bucketlist(self, current_user, bucketlist_key):
        """ remove a bucketlist via a bucketlist key .pop for list"""

        all_bucketlists[current_user].pop(bucketlist_key)


    def clear_bucketlist(self):
        """ Remove all items in the bucketlist """
        all_bucketlists[:] = []



class Bucketlist_Activities(Bucketlist):

    def __init__(self):
        super(Bucketlist_Activities, self).__init__()

    def create_bucketlist_activity(self, current_user, bucketlist_name, bucketlist_activity_name,
                                   due_date, done):

        new_activity = {bucketlist_activity_name: [done, due_date, bucketlist_name]}

        if current_user in all_bucketlists_activities:

            all_bucketlists_activities[current_user].append(new_activity)

        else:
            all_bucketlists_activities[current_user] = [new_activity]


    def update_bucketlist_activity(self, current_user, bucketlist_activity_key, bucketlist_name,
                                   due_date, bucketlist_activity_name, done):

        user_bucketlists_activities = all_bucketlists_activities[current_user]

        activity = user_bucketlists_activities[bucketlist_activity_key]

        activity = {bucketlist_activity_name: [done, due_date, bucketlist_name]}

        all_bucketlists_activities[current_user][bucketlist_activity_key] = activity




    def delete_bucketlist_activity(self, current_user, bucketlist_activity_key):

        all_bucketlists_activities[current_user].pop(bucketlist_activity_key)


# user1 = User()
# user1_bucketlist = Bucketlist()
# user1_bucketlist_activity = Bucketlist_Activities()

# user1.create_user("Zach Reed", "zreed@email.com", "qaz12#@")

# user1_bucketlist.create_bucketlist(all_users['zreed@email.com'][1],
#                                    'Career Things',
#                                    'Goals to achieve in my career')

# user1_bucketlist.create_bucketlist(all_users['zreed@email.com'][1],
#                                    'Travel Manenos',
#                                    'Places to travel')

# all_bucketlists_activities = {}
# user1_bucketlist_activity.create_bucketlist_activity(
#     all_users['zreed@email.com'][1],
#     'Career Things',
#     'Achieve A', '01/01/2018', False)

# user1_bucketlist_activity.create_bucketlist_activity(
#     all_users['zreed@email.com'][1],
#     'Career Things',
#     'Achieve XYZ', '01/01/2018', False)

# user1_bucketlist_activity.create_bucketlist_activity(
#     all_users['zreed@email.com'][1],
#     'Travel Manenos',
#     'Travel to A', '01/10/2018', False)



# user1_bucketlist_activity.update_bucketlist_activity(all_users['zreed@email.com'][1],
#                                                      0, 'Career Things', '01/02/2018',
#                                                      'Achieve Promotion', True)


# print(all_bucketlists_activities['zreed@email.com'])

# for activitylist in all_bucketlists_activities['zreed@email.com']:
#     for key, value in activitylist.items():
#         if value[2] == 'Travel Manenos':
#             print(key)
#             print("______________\n\n")
#             if value[0] == False:
#                 print("Not yet")
#             else:
#                 print("Done")
            
#             print("*****************")

