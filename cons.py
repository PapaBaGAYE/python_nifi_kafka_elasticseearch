from kafka import KafkaConsumer, consumer

my_topic_name = "test_gaye"
my_consumer_group = 'testid197'

kafka_servers = ("217.182.68.36:9092")
consum = KafkaConsumer(my_topic_name, my_consumer_group, bootstrap_servers=[kafka_servers], auto_offset_reset='earliest')
for msg in consum:
    print(msg)