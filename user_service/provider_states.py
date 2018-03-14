# STATES FOR TESTING
import json

from flask import Flask, request, Response, jsonify


def prepare_state(state):

    def write_to_file(row):
        file_path = "users.json"
        with open(file_path, 'w') as _f:
            json.dump(row, _f)
    if state == STATES[0] or state == STATES[1]:
        write_to_file({"data": ["User1", 123, "Editor"]})
    else:
        print("State {} is not implemented".format(state))


STATES = ['User1 exists and is not an administrator', 'User2 does not exist']

app = Flask(__name__)

STATUS = {
    'not_found': Response(status=404),
    'ok': Response(status=200)
}


@app.route('/provider_states', methods=['GET'])
def states():
    return jsonify({"LoginService": STATES})


@app.route('/provider_states/active', methods=['POST'])
def states_active():
    """ USAGE: python-verifier will send a request with the body:
               {consumer: 'Consumer name', states: ['a thing exists']}
               to this enpoint. One state at the time is allowed.
    """
    data = request.get_json()
    prepare_state(data["state"])

    return STATUS['ok']


if __name__ == '__main__':
    app.run(host='testing_states', port=5000)
