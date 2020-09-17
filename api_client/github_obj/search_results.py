# -*- coding: utf-8 -*-
#from __future__ import absolute_import
from __future__ import unicode_literals

#from six import text_type as str

#from yelp.obj.attribute import Attribute
#from yelp.obj.category import Category
#from yelp.obj.coordinates import Coordinates
#from yelp.obj.hours import Hours
#from yelp.obj.location import Location
from ..response_object import ResponseObject
from .stats import Stats
from .page_tracker import PageTracker
from .restaurant import Restaurant


class SearchResults(ResponseObject):

    _schema = {
        "listing_id": str,
        "stats": Stats,
        "pager": PageTracker,
        "results": [Restaurant],
        #"sponsored_result": SponsoredResult,
        #"market_context": MarketContext,
    }
