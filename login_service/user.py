import requests


USERS_URL = 'http://localhost:5002/users/'


def get_user(username):
    """Fetch a user object by user_name from the server."""
    uri = USERS_URL + username
    return requests.get(uri).json()
