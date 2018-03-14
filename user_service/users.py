import json

from flask import Flask, Response
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Users(Resource):

    def get(self, user_name):
        file_path = "users.json"
        with open(file_path, 'r') as _file:
            for line in _file:
                if json.loads(line)['data'][0] == user_name:
                    return json.loads(line)
        return Response(status=404)


api.add_resource(Users, '/users/<user_name>')  # Route_1

if __name__ == '__main__':
    app.run(host='api', port=5002)
