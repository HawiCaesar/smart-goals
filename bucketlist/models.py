# -*- coding: utf-8 -*-
import hashlib # Used for hashing

class User(object):
    def __init__(self, full_name, email, password):
        self.fullname = full_name
        self.email = email
        
        # make password into hash
        hash_object = hashlib.sha1(password.encode())
        self.password = hash_object.hexdigest()

        self.user_details = { self.fullname, self.email, self.password }


    # Get User details
    def getUser(self):
        return self.user_details



