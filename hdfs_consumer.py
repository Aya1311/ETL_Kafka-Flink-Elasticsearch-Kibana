# Import necessary libraries
from kafka import KafkaConsumer
from json import loads
import pydoop.hdfs as hdfs

# Create a Kafka consumer
consumer = KafkaConsumer(
    'topic_aya',  # Topic to consume messages from
    bootstrap_servers=['localhost:9092'],  # Kafka server addresses
    auto_offset_reset='earliest',  # Reset offset to the earliest available message
    enable_auto_commit=True,  # Enable auto commit of consumed messages
    group_id=None,  # Consumer group ID (None indicates an individual consumer)
)

hdfs_path = 'hdfs://localhost:9000/kafka_demo/tweets_data1.json'  # Path to the HDFS file

# Process incoming messages
for message in consumer:
    tweet = message.value  # Get the value of the message (tweet)
    print(tweet)  # Print the tweet

    with hdfs.open(hdfs_path, 'at') as file:
        print("Storing in HDFS!")
        file.write("{}\n".format(tweet))

