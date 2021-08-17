from flask import Flask
from sis_api.api.restplus import api
from sis_api.api.endpoints import ns


app = Flask(__name__)
api.init_app(app)
api.add_namespace(ns)
