"""CRUD Flask API Basic"""

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

list_data = []


class People(Resource):
    def __init__(self):
        pass

    def get(self, name):
        result = [value for value in list_data if value['Nome'] == name]
        if result:
            return result, 200
        return {"Nome": "Not found"}, 404

    def post(self, name):
        value = {'Nome': name}
        list_data.append(value)
        return value, 200

    def delete(self, name):
        for index, value in enumerate(list_data):
            if value["Nome"] == name:
                list_data.pop(index)
                return {"Deleted value": name}, 200
        return {"Deleted value": "Not found"}, 404


api.add_resource(People, "/names/<string:name>")  # http://127.0.0.1:8001/names/anynameyouwant

if __name__ == "__main__":
    app.run(port=8001, debug=True)
