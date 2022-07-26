from ensurepip import bootstrap
import json
import logging
import sys
sys.path.append('./')
import utils
from pydoc_data.topics import topics
from unicodedata import name
from kafka import KafkaProducer
from sseclient import SSEClient as EventSource
log = logging.getLogger()




class WikiProducer:

    def __init__(self):
        self.url = "https://stream.wikimedia.org/v2/stream/recentchange"
        self.bootstrap_server = '127.0.0.1:9092' 
        self.producers_dict = {}

    def run(self):

        for event in EventSource(self.url):
            if event.event == 'message':
                try:
                    content = json.loads(event.data)

                except ValueError as e:
                    print(e)
                    continue
                else:
                    producer = KafkaProducer(bootstrap_servers=[self.bootstrap_server],  
                                             value_serializer=lambda v: v.encode('utf-8'))
                    msg = json.dumps(content)
                    producer.send(topic=utils.TOPIC_NAME, value=msg)# value=content)

if __name__ == '__main__':
    wk = WikiProducer()
    wk.run()