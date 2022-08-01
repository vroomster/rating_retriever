# -*- coding: utf-8 -*-
from ..response_object import ResponseObject
from .rating import Rating
from .phone import Phone
from .address import Address

"""from __future__ import absolute_import
from __future__ import unicode_literals

from six import text_type as str

from yelp.obj.attribute import Attribute
from yelp.obj.category import Category
from yelp.obj.coordinates import Coordinates
from yelp.obj.hours import Hours
from yelp.obj.location import Location
from yelp.obj.response_object import ResponseObject"""


class Restaurant(ResponseObject):

    _schema = {
        "restaurant_id": str,
        "restaurant_hash": str,
        "name": str,
        "pickup": bool,
        "delivery": bool,
        "ratings": Rating,
        "phone_number": Phone,
        "address": Address,
        "merchant_url_path": str,

    }
