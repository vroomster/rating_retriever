# -*- coding: utf-8 -*-
#from __future__ import absolute_import
#from __future__ import unicode_literals

#from six import text_type as str

from ..response_object import ResponseObject
from .business import Business

class BusinessMatches(ResponseObject):

    _schema = {
        "businesses": [Business]
    }
