from sentry.auth.providers.oauth2 import OAuth2Provider, OAuth2Login, OAuth2Callback

from .constants import ACCESS_TOKEN_URL, AUTHORIZE_URL, CLIENT_ID, CLIENT_SECRET
from .views import FetchUser, ValidatePermissions


class GOVUKOAuth2Provider(OAuth2Provider):
    name = 'GOV.UK'
    access_token_url = ACCESS_TOKEN_URL
    authorize_url = AUTHORIZE_URL
    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET

    def get_auth_pipeline(self):
        return [
            OAuth2Login(
                authorize_url=self.authorize_url,
                client_id=self.client_id,
            ),
            OAuth2Callback(
                access_token_url=self.access_token_url,
                client_id=self.client_id,
                client_secret=self.client_secret,
            ),
            FetchUser(
                client_id=self.client_id,
                client_secret=self.client_secret,
            ),
            ValidatePermissions(),
        ]

    def build_config(self, state):
        return {}

    def build_identity(self, state):
        data = state['data']
        user = state['signon_user']
        return {
            'id': user['uid'],
            'email': user['email'],
            'name': user['name'],
            'data': self.get_oauth_data(data),
        }
