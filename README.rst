GOV.UK Signon authentication for Sentry
=======================================

A single sign-on provider to let you authenticate Sentry with
`GOV.UK Signon <https://github.com/alphagov/signonotron2/>`_.

Install
-------

::

    $ pip install https://github.com/alphagov/sentry-auth-govuk/archive/master.zip


Setup
-----

Create a new Signon application with the redirect URI set to something like this:

::

    https://sentry.dev.gov.uk/auth/sso/


Add some config to ``sentry.conf.py``:

.. code-block:: python

    GOVUK_SIGNON_UID = "uid"
    GOVUK_SIGNON_SECRET = "secret"
    GOVUK_SIGNON_BASE_DOMAIN = "https://signon.dev.gov.uk"
