# -*- coding: utf-8 -*-
import hashlib # Used for hashing

class User(object):
    # User created when __init__ runs

    def __init__(self, full_name, email, password):
        self.fullname = full_name
        self.email = email

        # make password into hash
        hash_object = hashlib.sha1(password.encode())
        self.password = hash_object.hexdigest()

        self.user_details = {'name':self.fullname, 'email':self.email, 'password': self.password}


    # Get User details
    def getUser(self):
        return self.user_details


    def updateUser(self, full_name, email):
        self.fullname = full_name
        self.email = email

        self.user_details['name'] = self.fullname
        self.user_details['email'] = self.email


        return self.user_details


class Bucketlist(object):
    all_bucketlists = [] # master bucketlist
    bucketlist = {}

    def create_bucketlist(self, bucketlist_name, bucketlist_description):
        """ Create a bucketlist and append it to the master bucketlist"""

        self.bucketlist[bucketlist_name] = bucketlist_description
        self.all_bucketlists.append({bucketlist_name:bucketlist_description})


    def get_bucketlists(self):
        """ Return master bucketlist """

        return self.all_bucketlists


    def update_bucketlist(self, bucketlist_key, bucketlist_name, bucketlist_description):
        """ get the bucket list key and update the new details of the bucketlist """

        update_bucklist = self.all_bucketlists[bucketlist_key]

        update_bucklist = {bucketlist_name: bucketlist_description}

        self.all_bucketlists[bucketlist_key] = update_bucklist

        return self.all_bucketlists


    def delete_bucketlist(self, bucketlist_key):
        """ remove a bucketlist via a bucketlist key .pop for lists"""

        self.all_bucketlists.pop(bucketlist_key)
        return self.all_bucketlists


    def clear_bucketlist(self):
        """ Remove all items in the bucketlist """
        self.all_bucketlists = []


class Bucketlist_Activities(Bucketlist):
    all_bucketlists_activities = [] # master bucketlist activity
    activity_details = {} # activity bucketlist

    def __init__(self):
        super(Bucketlist_Activities, self).__init__()

    def create_bucketlist_activity(self, bucketlist_key, bucketlist_activity_name,
                                   due_date, done):

        self.activity_details[bucketlist_activity_name] = {bucketlist_key:due_date}
        self.all_bucketlists_activities.append({bucketlist_activity_name:done})

    def get_bucketlist_ativities(self):
        return self.all_bucketlists_activities


    def get_bucketlists_activity_detail(self, bucketlist_activity_key):
        return self.activity_details[bucketlist_activity_key]


    def update_bucketlist_activity(self, all_bucketlist_activity_key,
                                   bucketlist_name,
                                   bucketlist_activity_name,
                                   due_date, done):

        self.all_bucketlists_activities[all_bucketlist_activity_key] = {
            bucketlist_activity_name:done}


        self.activity_details[bucketlist_activity_name] = {bucketlist_name:due_date}

        return self.all_bucketlists_activities

    def clear_bucketlist_activity(self):
        self.all_bucketlists_activities = []

    def delete_bucketlist_activity(self, bucketlist_activity_key):

        self.all_bucketlists_activities.pop(bucketlist_activity_key)
        return self.all_bucketlists_activities




# user5_bucketlist = Bucketlist()
# user5_bucketlist.clear_bucketlist()
# user5_bucketlist.create_bucketlist('Movie Watch', 'Must Watch these')
# user5_bucketlist.create_bucketlist('Attend 5 Live events', 'Site A, has all sites')

# print(len(user5_bucketlist.get_bucketlists()))
# user5_bucketlist.clear_bucketlist()
