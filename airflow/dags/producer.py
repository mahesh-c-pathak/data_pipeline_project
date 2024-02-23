def stream_data():
    from kafka import KafkaProducer
    import json
    import time
    import logging

    def get_registerd_user():
        from faker import Faker
        fake = Faker()
        return {
            "name":fake.name(),
            "address":fake.address(),
            "created_at":fake.year()
        }

    def json_serrializer(data):
        return json.dumps(data).encode("utf-8")

    producer = KafkaProducer(
        bootstrap_servers=['broker:29092'],
        value_serializer=json_serrializer)

    curr_time = time.time()
    while 1==1:
        if time.time() > curr_time + 60:
            break
        try:
            registered_user = get_registerd_user()
            print(registered_user)
            producer.send("quickstart-events", registered_user)
            time.sleep(4)
        except exception as e:
            logging.error(f"An error occured: {e}")
            continue

if __name__ == "__main__":
    stream_data()

        