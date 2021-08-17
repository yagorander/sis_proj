FROM solr:8.9.0-slim

RUN bin/solr start && \
    bin/solr create -c sis_texts

EXPOSE 8983