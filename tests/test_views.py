#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-helpscout
------------

Tests for `django-helpscout` helpers module.
"""

import json
from mock import patch, MagicMock
from django.test.client import Client
from django.test import TestCase
from django_helpscout import settings
from django_helpscout.views import helpscout_user, User


class TestHelpscoutView(TestCase):
    def setUp(self):
        settings.HELPSCOUT_SECRET = '1234'
        self.patcher = patch('django_helpscout.helpers.compare_digest')
        MockFunc = self.patcher.start()
        instance = MockFunc()
        instance.return_value = True

    def test_helpscout_user(self):
        request = MagicMock()
        request.method = 'POST'
        request.body = json.dumps({'customer': {'email': 'a@b.com'}})

        # User does not exist
        response = helpscout_user(request)
        self.assertTemplateUsed(response, 'django_helpscout/404.html')

        # User found
        user = User.objects.create(username='user1', email='a@b.com', password='1234')
        response = helpscout_user(request)
        self.assertTemplateUsed(response, 'django_helpscout/helpscout.html')

    def tearDown(self):
        self.patcher.stop()
