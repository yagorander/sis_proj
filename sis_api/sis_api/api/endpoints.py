from logging import INFO
from pysolr import SolrError
from aiologger import Logger
from asyncio import new_event_loop
from flask_restx import Resource, Namespace
from sis_api.api.utils import make_search, make_insert, response_error
from sis_api.api.models import index_input, search_input
from sis_api.api.log_config import log_config

ns = Namespace("", description="String Operations")
logger = Logger.with_default_handlers(level=INFO)
log_config(logger)

loop = new_event_loop()


@ns.route("/insert")
class IndexText(Resource):
    @ns.expect(index_input)
    def post(self, loop=loop):
        try:
            text = ns.payload["save_this"]
            if type(text) is not str:
                raise TypeError()
        except (KeyError, TypeError):
            message = "Invalid JSON. It must be like {'save_this': 'some text'}"
            return loop.run_until_complete(response_error(logger, message, 400))

        try:
            response = loop.run_until_complete(make_insert(text, logger))
        except SolrError:
            message = "Unable to connect to Solr"
            return loop.run_until_complete(response_error(logger, message, 500))
        except Exception:
            message = "Sorry! Something unexpected happend."
            return loop.run_until_complete(response_error(logger, message, 500))
        else:
            return response


@ns.route("/search")
class SearchText(Resource):
    @ns.expect(search_input)
    def post(self):
        try:
            text = ns.payload["search_for"]
            if type(text) is not str:
                raise TypeError()
        except (KeyError, TypeError):
            message = "Invalid JSON. It must be like {'search_for': 'some text'}"
            return loop.run_until_complete(response_error(logger, message, 400))

        try:
            response = loop.run_until_complete(make_search(text, logger))
        except SolrError:
            message = "Unable to connect to Solr"
            return loop.run_until_complete(response_error(logger, message, 500))
        except Exception:
            message = "Sorry! Something unexpected happend."
            return loop.run_until_complete(response_error(logger, message, 500))
        else:
            return response
