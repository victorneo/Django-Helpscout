from django.conf import settings
import logging


logger = logging.getLogger(__name__)


# Help Scout API secret key
HELPSCOUT_SECRET = getattr(settings, 'HELPSCOUT_SECRET', None)
