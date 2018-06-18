'''
name: usermanagement.py
author: Austin M. Crowley
author_email: devnodegree@gmail.com
'''

import hashlib

class User():

    def __init__(self, username):
        self.username=username
        self.__set_user_id()


    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __set_user_id(self):
        return hashlib.sha256(self.username)

class UserSession():

    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass