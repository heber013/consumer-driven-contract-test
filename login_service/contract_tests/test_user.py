import atexit
import unittest
from unittest.mock import patch

from pact import Consumer, Provider

from user import get_user

pact = Consumer('LoginService').has_pact_with(Provider('UserService'),
                                              host_name='localhost',
                                              port=1234,
                                              pact_dir='pacts')
pact.start_service()
atexit.register(pact.stop_service)


class TestGetUserInfoContract(unittest.TestCase):

    def test_get_user(self):
        expected = {"data": ["User1", 123, "Editor"]}

        (pact
         .given('User1 exists and is not an administrator')
         .upon_receiving('a request for User1')
         .with_request('get', '/users/User1')
         .will_respond_with(200, body=expected))
        pact.setup()
        # Patch USERS_URL so that the service uses the mock server URL instead of the real URL.
        with patch.dict('user.__dict__', {'USERS_URL': 'http://localhost:1234/users/'}):
            result = get_user('User1')
        pact.verify()
        self.assertEqual(result, expected)
