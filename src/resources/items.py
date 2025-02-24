import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items

itemBlueprint = Blueprint(
    "items",
    __name__,
    description="Operations on items",
)


@itemBlueprint.route("/items/<string:item_id>")
class Item(MethodView):
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message="Item not found")

    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted"}
        except KeyError:
            abort(404, message="Item not found")


@itemBlueprint.route("/items")
class ItemList(MethodView):
    def get(self):
        return {
            "items": list(items.values()),
        }

    def post():
        item_data = request.get_json()

        if (
            "price" not in item_data
            or "store_id" not in item_data
            or "name" not in item_data
        ):
            abort(400, message="Some properties are missing in the payload")

        item_id = uuid.uuid4().hex
        item = {
            **item_data,
            "id": item_id,
        }
        items[item_id] = item

        return item
