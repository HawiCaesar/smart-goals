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
    all_bucketlists = []

    def __init__(self):
        self.bucketlist = {}

    def create_bucketlist(self, bucketlist_name, bucketlist_description):
        self.bucketlist[bucketlist_name] = bucketlist_description
        self.all_bucketlists.append(self.bucketlist)

    def get_bucketlists(self):
        return self.all_bucketlists

    def update_bucketlist(self, bucketlist_key, bucketlist_name, bucketlist_description):
        update_bucklist = self.all_bucketlists[bucketlist_key]

        update_bucklist = {bucketlist_name: bucketlist_description}

        self.all_bucketlists[bucketlist_key] = update_bucklist

        return self.all_bucketlists

    def delete_bucketlist(self, bucketlist_key):
        self.all_bucketlists.pop(bucketlist_key)
        return self.all_bucketlists


    def clear_bucketlist(self):
        self.all_bucketlists = []

class Bucketlist_Activities(Bucketlist):
    def __init__(self):
        super(Bucketlist_Activities, self).__init__()
        self.bucketlist_activity_name = ''
        self.bucketlist_activity_description = ''
        self.bucketlist_activities = []
        self.done = False

    def create_bucketlist_activity(self, bucketlist_activity_name,
                                   bucketlist_description, due_date):
        pass

    def get_bucketlist_ativities(self):
        pass

    def update_bucketlist_activity(self):
        pass