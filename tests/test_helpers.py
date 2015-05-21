#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-helpscout
------------

Tests for `django-helpscout` helpers module.
"""

import hmac, hashlib, base64
from django.utils import unittest
from six import b
from mock import MagicMock
from django_helpscout import helpers, settings


class TestHelpscoutHelper(unittest.TestCase):
    def setUp(self):
        settings.HELPSCOUT_SECRET = '1234'

    def test_helpscout_request(self):
        # Compute signature for request body
        request_body = 'Request body'
        secret = settings.HELPSCOUT_SECRET
        dig = hmac.new(b(secret), msg=b(request_body),
                       digestmod=hashlib.sha1).digest()
        computed_sig = b(base64.b64encode(dig).decode())

        # Valid signature should return decorated function
        request = MagicMock()
        request.META = {'HTTP_X_HELPSCOUT_SIGNATURE': computed_sig}
        request.body = request_body

        decorator = helpers.helpscout_request(lambda x: True)
        self.assertTrue(decorator(request))

        # Should also work when header is a string
        request.META = {'HTTP_X_HELPSCOUT_SIGNATURE': str(computed_sig)}
        self.assertTrue(decorator(request))

        # Invalid signature should return a response code of 401
        request.META['HTTP_X_HELPSCOUT_SIGNATURE'] = u'234'
        response = decorator(request)
        self.assertEquals(401, response.status_code)
