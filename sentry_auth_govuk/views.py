from sentry.auth.view import AuthView

from .client import GOVUKSignonClient
from .constants import BASE_DOMAIN


class FetchUser(AuthView):
    def __init__(self, client_id, client_secret, *args, **kwargs):
        self.client = GOVUKSignonClient(client_id, client_secret, BASE_DOMAIN)
        super(FetchUser, self).__init__(*args, **kwargs)

    def handle(self, request, helper):
        access_token = helper.fetch_state('data')['access_token']

        user = self.client.get_user(access_token)

        helper.bind_state('signon_user', user)

        return helper.next_step()


class ValidatePermissions(AuthView):
    def handle(self, request, helper):
        user = helper.fetch_state('signon_user')

        if 'signin' in user['permissions']:
            return helper.next_step()
        else:
            return helper.error('You do not have permission to access Sentry in GOV.UK Signon.')
