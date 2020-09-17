# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from six import text_type as str

from ..response_object import ResponseObject


class Address(ResponseObject):

    _schema = {
        "street_address": str,
        "address_locality": str,
        "address_region": str,
        "postal_code": str,
        "address_country": str,
        "latitude": str,
        "longitude": str,
    }
