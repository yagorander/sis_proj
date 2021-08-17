import pysolr
from sis_api.api.log_config import log_info, log_error


def connect_solr():
    solr = pysolr.Solr("http://solr:8983/solr/sis_texts", always_commit=True)
    solr.ping()
    return solr


def index_text(text):
    solr = connect_solr()
    solr.add([{"text": text}])


def search_text(text):
    solr = connect_solr()
    results = solr.search(f"text:{text}", rows=500)
    num_found = results.raw_response["response"]["numFound"]
    found_list = [result["text"][0] for result in results.docs]
    found_dict = {"num_found": num_found, "strings_found": found_list}
    return found_dict


async def make_insert(text, logger):
    index_text(text)
    await log_info(logger, "Text successfully indexed!")
    return {"message": "Text successfully indexed!"}, 200


async def make_search(text, logger):
    results = search_text(text)
    strings_found = results["num_found"]
    await log_info(logger, f"{strings_found} strings were found.")
    return results, 200


async def response_error(logger, message, code):
    await log_error(logger, message)
    response = {"message": message}
    return response, code
