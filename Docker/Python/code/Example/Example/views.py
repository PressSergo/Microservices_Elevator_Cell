import logging
from django.http import HttpResponse
import pika
import pymongo

logger = logging.getLogger(__name__)


def test_view(request):
    logger.info('Something went wrong!')
    logger.debug('sasasa')
    print("wellDone")
    print("2341")
    return HttpResponse("hello")


def RabbitMQ(request):
    connection = pika.BlockingConnection(pika.URLParameters('amqp://guest:guest@message_brocker:5672'))
    channel = connection.channel()
    channel.queue_declare(queue='Test')

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(queue='Test',
                          auto_ack=True,
                          on_message_callback=callback)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    return HttpResponse("startRabbitMQ")


def MongoDb(request):
    myclient = pymongo.MongoClient("mongodb://mongo:27017/", username='admine', password='admine')
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mylist = [
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"},
        {"name": "Sandy", "address": "Ocean blvd 2"},
        {"name": "Betty", "address": "Green Grass 1"},
        {"name": "Richard", "address": "Sky st 331"},
        {"name": "Susan", "address": "One way 98"},
        {"name": "Vicky", "address": "Yellow Garden 2"},
        {"name": "Ben", "address": "Park Lane 38"},
        {"name": "William", "address": "Central st 954"},
        {"name": "Chuck", "address": "Main Road 989"},
        {"name": "Viola", "address": "Sideway 1633"}
    ]

    x = mycol.insert_many(mylist)

    # print list of the _id values of the inserted documents:
    print(x.inserted_ids)
    return HttpResponse("MongoDB")
