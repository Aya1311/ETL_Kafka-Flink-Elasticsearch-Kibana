from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import requests
from json import dumps
from kafka import KafkaProducer
from time import sleep
from newsapi import NewsApiClient

url = ''
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda K:dumps(K).encode('utf-8'))
# Parameters to get the first 10 repositories
# Init
newsapi = NewsApiClient(api_key='49c02fcde33f41a4b5c093011c4e7b91')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines()

for data in top_headlines["articles"]:
    print("\n")
    print (data)
    producer.send('topic_aya', value=data)
    sleep(0.5)

