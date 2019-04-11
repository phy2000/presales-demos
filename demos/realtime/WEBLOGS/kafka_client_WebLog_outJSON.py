"""

"""
from kafka import KafkaConsumer
import json
import sys

#print sys.getdefaultencoding()
print ("Listening to Kafka topic <WebLog_outJSON>...")
# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('WebLog_outJSON',
                         group_id='my-group',
                         bootstrap_servers=['napslxcdh01:9092'], 
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    # consume json messages
    #KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))
    #KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    #ustr=message.value.decode('utf-8')
    print ("topic=%s partition=%d offset=%d key=%s value=%s" % (message.topic, message.partition, message.offset, message.key, json.dumps(message.value, encoding='utf-8')))
    #test=json.dumps(message.value, encoding='utf-8')
    #print (test)
    print ("-----------------------")

# consume earliest available messages, don't commit offsets
#KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)

# consume msgpack
#KafkaConsumer(value_deserializer=msgpack.unpackb)

# StopIteration if no message after 1sec
#KafkaConsumer(consumer_timeout_ms=1000)
