# -*- coding: utf-8 -*-
#from __future__ import absolute_import
#from __future__ import unicode_literals

#from six import text_type as str

from .attribute import Attribute
from .category import Category
from .coordinates import Coordinates
from .hours import Hours
from .location import Location
from ..response_object import ResponseObject


class Business(ResponseObject):

    _schema = {
        "id": str,
        "alias": str,
        "name": str,
        "image_url": str,
        "is_claimed": bool,
        "is_closed": bool,
        "url": str,
        "phone": str,
        "display_phone": str,
        "review_count": int,
        "categories": [Category],
        "rating": float,
        "location": Location,
        "coordinates": Coordinates,
        "photos": [str],
        "hours": [Hours],
        "transactions": [str],
        "attributes": [Attribute],
    }
