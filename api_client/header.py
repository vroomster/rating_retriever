# -*- coding: utf-8 -*-
#from __future__ import absolute_import
#from __future__ import unicode_literals
#import six

#from yelp.config import API_ROOT_URL
#from yelp.endpoint.business import BusinessEndpoints
#from yelp.errors import YelpError


class Header:

    def __init__(self, headers={}, api_key=None, add_content_type_json=False):
        self.headers = headers
        if api_key:
            self.add_auth_header(api_key)
        if add_content_type_json:
            self.add_content_type_json()

    def add_auth_header(self, api_key):
        self.headers["Authorization"] = "Bearer {api_key}".format(api_key=api_key)

    def add_content_type_json(self):
        self.headers['Content-Type'] = 'application/json'
