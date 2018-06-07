import csv
from elasticsearch import helpers, Elasticsearch

es = Elasticsearch()

with open('tweetsentiments.csv') as f:
    reader = csv.DictReader(f)
    helpers.bulk(es, reader, index='index13', doc_type='type')
