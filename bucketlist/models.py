
class User(object):
    def __init__(self, full_name, email, password):
        self.fullname = full_name
        self.email = email
        self.password = password

        self.user_details = { self.fullname, self.email, self.password }

    # Get User details
    def getUser(self):
        return self.user_details
