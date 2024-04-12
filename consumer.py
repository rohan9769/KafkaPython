from kafka import KafkaConsumer
from json import loads
import json

consumer = KafkaConsumer('youtube',bootstrap_servers=['192.168.1.214:9092'],api_version=(0,10,1))

for message in consumer:
    print(message.value)

