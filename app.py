"""
TODO
1. fix formatting
2. fix location of app.py
3. fix auto initializing of venv when opening a terminal
4. docker-compose -f <file> -f <file for overriding>
"""

from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 15.99,
            }
        ],
    }
]


@app.get("/stores")
def get_stores():
    data = {"stores": stores}
    print("haha")
    return data, 200


@app.post("/stores")
def post_stores():
    request_data = request.get_json()
    new_store = {
        "name": request_data["name"],
        "items": [],
    }
    stores.append(new_store)
    return new_store, 201


@app.get("/stores/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store, 200
    return {
        "message": "Store not found",
    }, 404


@app.get("/stores/<string:name>/items")
def get_store_items(name):
    for store in stores:
        if store["name"] == name:
            return {
                "items": store["items"],
            }
    return {
        "message": "Store not found",
    }, 404


@app.post("/stores/<string:name>/items")
def post_store_item(name):
    request_data = request.get_json()

    for store in stores:
        if store["name"] == name:
            new_item = {
                "name": request_data["name"],
                "price": request_data["price"],
            }
            store["items"].append(new_item)
            return new_item, 201

    return {
        "message": "Store not found",
    }, 404
