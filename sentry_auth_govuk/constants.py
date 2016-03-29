from django.conf import settings

CLIENT_ID = getattr(settings, 'GOVUK_SIGNON_UID', None)
CLIENT_SECRET = getattr(settings, 'GOVUK_SIGNON_SECRET', None)

BASE_DOMAIN = getattr(settings, 'GOVUK_SIGNON_BASE_DOMAIN', None)

ACCESS_TOKEN_URL = '{0}/oauth/token'.format(BASE_DOMAIN)
AUTHORIZE_URL = '{0}/oauth/authorize'.format(BASE_DOMAIN)
