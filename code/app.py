from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)  # To easily add Resource's

# In memory database
items = []


class Item(Resource):
    # Iterate through items in the database
    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, items), None)
        # for item in items:
        #     if item['name'] == name:
        #         return item
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None):
            return {"message': 'An item with name '{}' already exists.".format(name)}, 400

        data = request.get_json(force=True)  # Doesnt need content-type header
        item = {'name': name, 'price': data['price']}  # Accesses price key of data dictionary
        items.append(item)
        return item, 201  # Created successfully


class ItemList(Resource):
    def get(self):
        return {'items': items}  # Return dictionary of items


api.add_resource(Item, '/item/<string:name>')  # make accessible with API
api.add_resource(ItemList, '/items')

app.run(port=5000, debug=True)  # Debug active
