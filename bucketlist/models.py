# -*- coding: utf-8 -*-
import hashlib # Used for hashing
all_users = []
all_bucketlists = []
all_bucketlists_activities = []

class User(object):
    # User created when __init__ runs

    def create_user(self, full_name, email, password):
        self.fullname = full_name
        self.email = email

        # make password into hash
        hash_object = hashlib.sha1(password.encode())
        self.password = hash_object.hexdigest()

        all_users.append({'name':self.fullname, 'email':self.email, 'password': self.password})

    # Get User details
    def getUser(self):
        return all_users


    def updateUser(self, user_key, full_name, email):
        self.fullname = full_name
        self.email = email

        update_user = all_users[user_key]
        update_user = {'name':self.fullname, 'email':self.email, 'password': self.password}

        all_users[user_key] = update_user

        return all_users

    def clear_users(self):
        all_users[:] = []

class Bucketlist(object):
     # master bucketlist
    bucketlist = {}

    def create_bucketlist(self, bucketlist_name, bucketlist_description):
        """ Create a bucketlist and append it to the master bucketlist"""

        self.bucketlist[bucketlist_name] = bucketlist_description
        all_bucketlists.append({bucketlist_name:bucketlist_description})


    def get_bucketlists(self):
        """ Return master bucketlist """

        return all_bucketlists


    def update_bucketlist(self, bucketlist_key, bucketlist_name, bucketlist_description):
        """ get the bucket list key and update the new details of the bucketlist """

        update_bucklist = all_bucketlists[bucketlist_key]

        update_bucklist = {bucketlist_name: bucketlist_description}

        all_bucketlists[bucketlist_key] = update_bucklist

        return all_bucketlists


    def delete_bucketlist(self, bucketlist_key):
        """ remove a bucketlist via a bucketlist key .pop for lists"""

        all_bucketlists.pop(bucketlist_key)
        return all_bucketlists


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


user1_bucketlist = Bucketlist()
user1_bucketlist.clear_bucketlist()
user1_bucketlist.create_bucketlist('Career Things', 'Goals to achieve in my career')


user2_bucketlist = Bucketlist()
user2_bucketlist.clear_bucketlist()
user2_bucketlist.create_bucketlist("Traveling", "Places to visit")

print(all_bucketlists)