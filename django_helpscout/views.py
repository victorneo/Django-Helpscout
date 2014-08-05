# -*- coding: utf-8 -*-
import json
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.http import require_http_methods
from django_helpscout.helpers import helpscout_request


User = get_user_model()


@require_http_methods(['POST'])
@helpscout_request
def helpscout_user(request, template_name='django_helpscout/helpscout.html',
                   template_name_404='django_helpscout/404.html'):
    """
Displays a user's information for Help Scout's custom app integration.
Optional Arguments:
``template_name``: name of the template to use.
``template_name_404``: name of the template to use when user does not exist
"""
    email = json.loads(request.body)['customer']['email']

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        rendered = render_to_string(template_name_404)
    else:
        rendered = render_to_string(template_name, user)

    return HttpResponse(json.dumps({'html': rendered}),
                        content_type="application/json")
