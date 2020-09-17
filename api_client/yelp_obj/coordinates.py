# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

from ..response_object import ResponseObject


class Coordinates(ResponseObject):

    _schema = {"latitude": float, "longitude": float}
