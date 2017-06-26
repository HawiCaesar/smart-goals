# -*- coding: utf-8 -*-
import hashlib # Used for hashing
all_users = {}
all_bucketlists = {}
all_bucketlists_activities = []

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


    # def get_bucketlists(self):
    #     """ Return master bucketlist """

    #     return all_bucketlists


    def update_bucketlist(self, user_key, bucketlist_key,
                          new_bucketlist_name, new_bucketlist_description):

        """ get the bucket list key and update the new details of the bucketlist """

        user_bucketlists = all_bucketlists[user_key]

        update_bucketlist = user_bucketlists[bucketlist_key]

        update_bucketlist = {new_bucketlist_name:new_bucketlist_description}

        all_bucketlists[user_key][bucketlist_key] = update_bucketlist



    def delete_bucketlist(self, user_key, bucketlist_key):
        """ remove a bucketlist via a bucketlist key .pop for list"""

        all_bucketlists[user_key].pop(bucketlist_key)


    def clear_bucketlist(self):
        """ Remove all items in the bucketlist """
        all_bucketlists[:] = []



class Bucketlist_Activities(Bucketlist):
     # master bucketlist activity
    activity_details = {} # activity bucketlist

    def __init__(self):
        super(Bucketlist_Activities, self).__init__()

    def create_bucketlist_activity(self, bucketlist_key, bucketlist_activity_name,
                                   due_date, done):

        self.activity_details[bucketlist_activity_name] = {bucketlist_key:due_date}
        all_bucketlists_activities.append({bucketlist_activity_name:done})

    def get_bucketlist_ativities(self):
        return all_bucketlists_activities


    def get_bucketlists_activity_detail(self, bucketlist_activity_key):
        return self.activity_details[bucketlist_activity_key]


    def update_bucketlist_activity(self, all_bucketlist_activity_key,
                                   bucketlist_name,
                                   bucketlist_activity_name,
                                   due_date, done):

        all_bucketlists_activities[all_bucketlist_activity_key] = {
            bucketlist_activity_name:done}


        self.activity_details[bucketlist_activity_name] = {bucketlist_name:due_date}

        return all_bucketlists_activities

    def clear_bucketlist_activity(self):
        all_bucketlists_activities[:] = []

    def delete_bucketlist_activity(self, bucketlist_activity_key):

        all_bucketlists_activities.pop(bucketlist_activity_key)
        return all_bucketlists_activities

user1 = User()
user1.create_user("John Ist", "jist@email.com", "qaz12#@")

user1_bucketlist = Bucketlist()

user1_bucketlist.create_bucketlist(all_users['jist@email.com'][1],
                                   'Career Things',
                                   'Goals to achieve in my career')
user1_bucketlist.create_bucketlist(all_users['jist@email.com'][1],
                                   'Travel Manenos',
                                   'Places to travel')

user1_bucketlist.update_bucketlist('jist@email.com', 0, '', '')

print(all_bucketlists['jist@email.com'])
#print(len(all_bucketlists['jist@email.com']))