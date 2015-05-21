from functools import wraps
import base64, hmac, hashlib
from six import b, PY3
from django.http import HttpResponse
from django_helpscout import settings


try:
    # compare_digest is only available in Python >= 2.7.7
    from hmac import compare_digest
except ImportError:
    # Use unsafe String comparison function for Python < 2.7.7
    compare_digest = lambda x, y: x == y


def helpscout_request(f):
    """Determines if a incoming request if from Help Scout using
    X-HelpScout-Signature.

    Returns HTTP 401 if signature is invalid.
    """
    @wraps(f)
    def decorated_function(request, *args, **kwargs):
        helpscout_sig = request.META.get('HTTP_X_HELPSCOUT_SIGNATURE')
        secret = b(settings.HELPSCOUT_SECRET)
        request_body = b(request.body)

        h = hmac.new(secret, msg=request_body, digestmod=hashlib.sha1)
        dig = h.digest()
        computed_sig = b(base64.b64encode(dig).decode())

        if PY3 and type(helpscout_sig) == str:
            helpscout_sig = bytes(helpscout_sig, 'utf-8')

        if not compare_digest(computed_sig, helpscout_sig):
            return HttpResponse(status=401)

        return f(request, *args, **kwargs)
    return decorated_function
