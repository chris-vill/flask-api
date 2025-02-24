"""
TODO
1. fix formatting
2. fix location of app.py
3. fix auto initializing of venv when opening a terminal
4. docker-compose -f <file> -f <file for overriding>
"""

from flask import Flask
from flask_smorest import Api
from resources.items import itemBlueprint
from resources.stores import storeBlueprint

app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

api = Api(app)

api.register_blueprint(itemBlueprint)
api.register_blueprint(storeBlueprint)
