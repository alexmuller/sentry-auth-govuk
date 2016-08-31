from sentry import http
from sentry.utils import json


class GOVUKSignonClient(object):
    def __init__(self, client_id, client_secret, base_domain):
        self.base_domain = base_domain
        self.client_id = client_id
        self.client_secret = client_secret
        self.http = http.build_session()

    def get_user(self, access_token):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
        }

        headers = {
            'Authorization': 'Bearer {0}'.format(access_token),
        }

        req = self.http.get(
                '{0}/user.json?client_id={1}'.format(self.base_domain, self.client_id),
                params=params,
                headers=headers,
              )

        return json.loads(req.content)['user']
