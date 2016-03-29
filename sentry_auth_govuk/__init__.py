from sentry.auth import register

from .provider import GOVUKOAuth2Provider

register('govuk', GOVUKOAuth2Provider)
