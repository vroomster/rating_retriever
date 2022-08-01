# -*- coding: utf-8 -*-
#from __future__ import absolute_import
#from __future__ import unicode_literals

import requests
#import six

#from yelp.config import API_ROOT_URL
#from yelp.endpoint.business import BusinessEndpoints
#from yelp.errors import YelpError


class Client(object):
    def __init__(self, header):
        self._session = requests.Session()
        self._session.headers.update(header.headers)

    def make_get_request(self, url, params=None, error_handler=None):
        response = self._session.get(url, params=params)
        #print(response)
        #print(response.text)
        return response

    def make_post_request(self, base_url, data=None, json=None):
        response = self._session.post(url, data=data, json=json)
        return response


'''
        if response.status_code == 200:
            return response.json()
        else:
            raise YelpError.from_response(response)
'''
