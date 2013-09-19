# -*- coding: utf-8 -*-

__author__ = 'lahim'


class Facebook(object):
    def __init__(self, id):
        self.client_id = id

    def get_funs_number(self):
        return 400


class FacebookClient(Facebook):
    def __init__(self, id):
        super(FacebookClient, self).__init__(id)

    @property
    def funs_number(self):
        return self.get_funs_number()


fb_client = FacebookClient('Technopark_Pomerania')

if fb_client.funs_number >= 400:
    print "Thank you!"