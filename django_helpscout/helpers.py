from functools import wraps
import hmac
import hashlib
import base64
from django.http import HttpResponse
from django_helpscout import settings


try:
    # compare_digest is only available in Python 2.7.7
    from hmac import compare_digest
except ImportError:
    # Use unsafe String comparison function for Python < 2.7.7
    compare_digest = lambda x, y: x == y


def helpscout_request(f):
    """Determines if a incoming request if from Help Scout using
    X-HelpScout-Signature. Returns HTTP 401 if signature is
    invalid.
    """
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        helpscout_sig = request.META.get('X-Helpscout-Signature')
        secret = settings.HELPSCOUT_SECRET

        dig = hmac.new(secret, msg=request.body,
                       digestmod=hashlib.sha1).digest()
        computed_sig = base64.b64encode(dig).decode()

        if not compare_digest(computed_sig, helpscout_sig):
            return HttpResponse(status=401)

        return f(request, *args, **kwargs)
    return decorated_function

