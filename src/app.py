"""
TODO
1. fix formatting
2. fix location of app.py
3. fix auto initializing of venv when opening a terminal
4. docker-compose -f <file> -f <file for overriding>
"""

import uuid
from flask import Flask, request
from db import items, stores

app = Flask(__name__)


@app.get("/stores")
def get_stores():
    return {"stores": list(stores.values())}, 200


@app.post("/stores")
def create_stores():
    store_id = uuid.uuid4().hex
    new_store = {
        **request.get_json(),
        "id": store_id,
    }
    stores[store_id] = new_store
    return new_store, 201


@app.get("/stores/<string:id>")
def get_store(id):
    try:
        return stores[id]
    except KeyError:
        return {
            "message": "Store not found",
        }, 404


@app.get("/items")
def get_items():
    return {
        "items": list(items.values()),
    }, 200


@app.get("/items/<string:id>")
def get_item():
    try:
        return items[id]
    except KeyError:
        return {
            "message": "Item not found",
        }, 404


@app.post("/items")
def create_item():
    item_data = request.get_json()

    if item_data["store_id"] not in stores:
        return {
            "message": "Store not found",
        }, 404

    item_id = uuid.uuid4().hex
    item = {
        **item_data,
        "id": item_id,
    }
    items[item_id] = item

    return item, 201
