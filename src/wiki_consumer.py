from kafka import KafkaConsumer
import json
import utils

class WikiConsumer:

    def __init__(self, topic) -> None:
        self.topic = topic
        self.bootstrap_server = '127.0.0.1:9092'
        self.counter = 0
        self.domain_dict = {}

    def run(self):
        consumer = KafkaConsumer(self.topic,
                                 bootstrap_servers=[self.bootstrap_server], 
                                 value_deserializer=lambda v: v.decode('utf-8'))
        for msg in consumer:
            msg = json.loads(msg.value)
            domain_name = msg['meta']['domain']
            # print(msg)
            if domain_name in self.domain_dict:
                self.domain_dict[domain_name] += 1
            else:
                self.domain_dict[domain_name] = 1
            yield {domain_name: self.domain_dict[domain_name]}


if __name__ == '__main__':
    topic = 'commons-wikimedia-org'
    wk = WikiConsumer(topic)
    wk.run()

