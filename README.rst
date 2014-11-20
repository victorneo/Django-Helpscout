=============================
Django-Helpscout
=============================

.. image:: https://travis-ci.org/victorneo/Django-Helpscout.svg?branch=master
    :target: https://travis-ci.org/victorneo/Django-Helpscout

.. image:: https://img.shields.io/coveralls/victorneo/Django-Helpscout.svg
    :target: https://coveralls.io/r/victorneo/Django-Helpscout?branch=master 

Help Scout integration for Django.

Introduction
-------------

If you are using Help Scout to handle support tickets from your users for your Django
web application, you can use Help Scout's custom app feature to provide information
on the user, such as the following:

.. image:: https://raw.githubusercontent.com/victorneo/Django-Helpscout/master/helpscout_customapp.png

This project provides a Django app which allows you to integrate Custom App into your
Django web application and easily customize the output HTML.

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
Help Scout custom app URL to the url you have configured above and
you should see a simple HTML output on Help Scout with the user's
username and date joined.

Customizing the HTML Output
---------------------------

You will most likely want to customize the HTML output to add in
additional information related to the user. This library provides
an easy way for you to override the templates that are used.

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

By adding your own templates and effectively overriding the library's
built-in templates, you can customize the output to suit your needs.

Further Customizations
----------------------

You might want to use ``select_related`` to prefetch related models
for a particular user, or you have complicated processing involved
when loading a user. A helper decorator is available if you wish to
use your own views.

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

Copyright 2014 Victor Neo

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
