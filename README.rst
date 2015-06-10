=============================
Django-Helpscout
=============================

.. image:: https://travis-ci.org/victorneo/Django-Helpscout.svg?branch=master
    :target: https://travis-ci.org/victorneo/Django-Helpscout

.. image:: https://img.shields.io/coveralls/victorneo/Django-Helpscout.svg
    :target: https://coveralls.io/r/victorneo/Django-Helpscout?branch=master 

.. image:: https://img.shields.io/pypi/dw/Django-Helpscout.svg
    :target: https://pypi.python.org/pypi/django-helpscout/

.. image:: https://img.shields.io/pypi/v/Django-Helpscout.svg
    :target: https://pypi.python.org/pypi/django-helpscout/

Help Scout integration for Django.

Introduction
-------------

If you are using Help Scout to handle support tickets for your Django
web application, you can use Help Scout's custom app feature to provide
additional information on the user, such as the following:

.. image:: https://raw.githubusercontent.com/victorneo/Django-Helpscout/master/helpscout_customapp.png

This project provides a Django app which allows you to integrate Help Scout
Custom App into your Django web application and easily customize the output.

Installation
-------------

You can install this library via ``pip``::

    pip install django-helpscout

Once installed, add ``django_helpscout`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'django_helpscout'
        ...,
    )

Add Help Scout's secret key to your settings file::

    HELPSCOUT_SECRET = '<helpscout custom app secret key>'


Getting Started
----------------

A Django view is provided to make it easy for you to get started. First, add
the view to your ``urls.py``::

    from django_helpscout.views import helpscout_user

    urlpatterns = patterns('',
        # Your URL definitions
        url(r'^helpscout-user/$', helpscout_user),
    )

Once done, deploy your web application to production and point your
Help Scout Custom App URL to the url you have configured above and
you should see a simple HTML output on the side bar of a support ticket with
the user's username and join date.

Customizing the HTML Output
---------------------------

You will want to customize the HTML output to add in additional information
related to the user. You can do so by overriding the templates that are
included.

In your templates folder, create the following structure::

    templates/
        |- django_helpscout
                 |- 404.html
                 |- helpscout.html

Details on the two templates:

``404.html``
  Used when a user with the given email address is not found

``helpscout.html``
  Used when a user is found

By overriding the library's built-in templates, you can customize the output to
suit your needs.

Further Customizations
----------------------

You might want to use ``select_related`` to prefetch related models
for a particular user, or you have additional data sources to query
when loading a user. A helper decorator is available if you wish to
use your own view.

The decorator helps you deal with verifying Help Scout's signature
when a request is made from their side. You can use the decorator
in the following manner::

    from django_helpscout.helpers import helpscout_request

    # your view
    @helpscout_request
    def load_user_for_helpscout(request):
        ... code here ...


License
-------

Copyright 2015 Victor Neo

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
