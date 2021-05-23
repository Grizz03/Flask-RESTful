from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)  # To easily add Resource's

# In memory database
items = []


class Items(Resource):
    # Iterate through items in the database
    def get(self, name):
        for item in items:
            if item['name'] == name:
                return item
        return {'items': None}, 404  # Not found

    def post(self, name):
        item = {'name': name, 'price': 12.00}
        items.append(item)
        return item, 201  # Created successfully


api.add_resource(Items, '/item/<string:name>')  # make accessible with API

app.run(port=5000)
