from flask_restx import fields
from sis_api.api.restplus import api


index_input = api.model("Index", {"save_this": fields.String(required=True, description="string to index")})

search_input = api.model("Search", {"search_for": fields.String(required=True, description="string to search for")})
