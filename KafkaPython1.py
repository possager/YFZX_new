from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import json

class Kafka_producer():

    #kafka producer

    def __init__(self, kafkatopic):
        self.kafkaHost = "192.168.6.187,192.168.6.188,192.168.6.229,192.168.6.230"
        self.kafkaPort = 9092
        self.kafkaTopic = kafkatopic
        self.producer = KafkaProducer(bootstrap_servers='{kafka_host}:{kafka_port}'.format(
            kafka_host=self.kafkaHost,
            kafka_port=self.kafkaPort
        ))

    def produce_data(self, data):
        try:
            parmas_message = json.dumps(data)
            producer = self.producer
            #producer.send(self.kafkaTopic, parmas_message.encode('utf-8'))
            producer.send(self.kafkaTopic, parmas_message)
            producer.flush()
        except KafkaError as e:
            print e


class Kafka_consumer():

    #kafka consumer

    def __init__(self,kafkatopic,groupid):
        self.kafkaHost = "192.168.6.187,192.168.6.188,192.168.6.229,192.168.6.230"
        self.kafkaPort = 9092
        self.kafkaTopic = kafkatopic
        self.groupId = groupid
        self.consumer=KafkaConsumer(self.kafkaTopic,group_id=self.groupId,
                                    bootstrap_servers='{kafka_host}:{kafka_port}'.format(
                                        kafka_host=self.kafkaHost,
                                        kafka_port=self.kafkaPort
                                    ))

    def consume_data(self):
        print "consumer_OK"
        try:
            for message in self.consumer:
                yield message
                print message
                print "OK1"
        except  KeyboardInterrupt,e:
            print e


def main():
    consumer=Kafka_consumer("test","testgroup3")
    message=consumer.consume_data()
    print "OK2"
    for mm in message:
        print"oK3"
        print mm.value

if __name__=='__main__':
    main()