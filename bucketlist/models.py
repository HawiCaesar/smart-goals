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
    def __init__(self):
        self.bucketlists = []

    def create_bucketlist(self, bucketlist_name, bucketlist_description):
        self.bucketlists.append({bucketlist_name:bucketlist_description})

    def get_bucketlists(self):
        return self.bucketlists

    def update_bucketlist(self, bucketlist_key, bucketlist_name, bucketlist_description):
        update_bucklist = self.bucketlists[bucketlist_key]

        update_bucklist = {bucketlist_name: bucketlist_description}

        self.bucketlists[bucketlist_key] = update_bucklist

        return self.bucketlists
    
    def delete_bucketlist(self, bucketlist_key):
        self.bucketlists.pop(bucketlist_key)
        return self.bucketlists

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