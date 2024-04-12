from kafka import KafkaProducer
from time import sleep
import json
from datetime import datetime

producer = KafkaProducer(bootstrap_servers=['192.168.1.214:9092'],api_version=(0,10,1))

producer.send('youtube',b'Hello World this is youtube')
producer.flush()

now = datetime.now()
print(now)
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
print(current_time)
for i in range(10):
    message = 'Message {}'.format(str(datetime.now().time()))
    producer.send('youtube',json.dumps(message).encode('utf-8'))
    sleep(2)
    print('Message sent',i)
