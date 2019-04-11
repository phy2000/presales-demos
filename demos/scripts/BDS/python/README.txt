------------------------------
Usage: tstream.py [-f SEARCHPATTERN]
Stream twitter with optional filter pattern. Return up to 1000 records.
Options:
  -h, --help        show this help message and exit
  -f SEARCHPATTERN  search pattern to filter input
------------------------------
Usage: tsearch.py [-f SEARCHPATTERN]
Search twitter for given search pattern. Return up to 10 records.
Options:
  -h, --help        show this help message and exit
  -f SEARCHPATTERN  search pattern to filter input
------------------------------
Usage: kafkaListTopic.py [ -b HOST:PORT] 
List Kafka Topics, default broker at localhost:9092
Options:
  -h, --help  show this help message and exit
  -b BROKER   kafka broker in <host>:<port> format
------------------------------
Usage: kafkaProducer.py -t TOPIC [-b HOST:PORT] 
Kafka producer on given topic, default broker at localhost:9092
Options:
  -h, --help  show this help message and exit
  -t TOPIC    kafka topic to send
  -b BROKER   kafka broker in <host>:<port> format
------------------------------
Usage: kafkaConsumer.py -t TOPIC [-b HOST:PORT] 
Kafka consumer on given topic, default broker at localhost:9092
Options:
  -h, --help  show this help message and exit
  -t TOPIC    kafka topic to listen
  -b BROKER   kafka broker in <host>:<port> format
------------------------------
Usage: kinesisProducer.py -t streamname 
Options:
  -h, --help     show this help message and exit
  -n STREAMNAME  stream name to send to
------------------------------
Usage: kinesisConsumer.py -n streamname
Options:
  -h, --help     show this help message and exit
  -n STREAMNAME  stream name to read from
------------------------------
Usage: kinesisListTopic.py
    List up to 1000 stream names
------------------------------
