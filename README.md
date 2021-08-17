# SIS - String Indexer and Searcher

SIS is a simple project that can both save and search for texts. 
The project consists of two services: 
* SIS API
* Solr container

SIS uses a Solr container to store and then retrieve the texts searching for occurring terms. The Solr search engine is pretty fast and easy to use. The SIS API makes it easier to interact with the Solr container.

The project requires `Docker` and `docker-compose` installed on the machine.
To run the project on your machine clone this repo and run the command below on the project root folder:
```sh
docker-compose up --build
```

This will build and start both services (SIS API and Solr).

The SIS API has two endpoints:

## **/insert** (POST METHOD)
Complete URL: http://localhost:5000/insert

Request body:
```json
{
    "save_this": "Text to be saved."
}
```

## **/search** (POST METHOD)
Complete URL: http://localhost:5000/search

Request body:
```json
{
    "search_for": "these words"
}
```

There is also the GUI API documentation endpoint available on http://localhost:5000/docs . It shows the endpoints and request parameters patterns. It is also possible to make requests using the GUI.

![API_GUI](https://user-images.githubusercontent.com/46166518/129746661-acf7194e-2a20-458b-875a-e5d3aa6ea48e.png)

---

## LOGS

The API logs are asynchronously generated and exposed on the host machine filesystem at `logs/sis.log`

## *That's it!*
