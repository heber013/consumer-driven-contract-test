import requests


USERS_URL = 'http://localhost:5002/users/'


def get_user(username):
    """Fetch a user object by user_name from the server."""
    uri = USERS_URL + username
    response = requests.get(uri)
    return response.json() if response.status_code == 200 else response
