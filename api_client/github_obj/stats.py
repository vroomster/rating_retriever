# -*- coding: utf-8 -*-
#from __future__ import absolute_import
from __future__ import unicode_literals

from ..response_object import ResponseObject

#from six import text_type as str

#from yelp.obj.attribute import Attribute
#from yelp.obj.category import Category
#from yelp.obj.coordinates import Coordinates
#from yelp.obj.hours import Hours
#from yelp.obj.location import Location
#from yelp.obj.response_object import ResponseObject


class Stats(ResponseObject):

    _schema = {
        "total_results": int,
        "result_count": int,
        "page_size": int,
        "total_hits": int,
    }
