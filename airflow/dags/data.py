
def callable_virtualenv():
    from time import sleep
    from faker import Faker
    from kafka import KafkaProducer
    fake = Faker()
    print(fake.name())
    print(fake.address())
    print(fake.year())
    print("Finished")