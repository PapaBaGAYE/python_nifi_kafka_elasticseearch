from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=["217.182.68.36:9092"], api_version=(2,5,0))
producer.send('test_gaye', b'{"location":"12.76, -13.76", "typeProduit":"ordi", "price":200500}')
producer.flush()

