import pika
import json
class testRpcClient(object):
    def __init__(self):
        with open("/home/ubuntu/jgiraldop-st0263/gateWay/config.json", "r") as jsonfile:
            self.config = json.load(jsonfile)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.config['response_queue'])
        self.channel.basic_consume(
            queue=self.config['response_queue'],
            on_message_callback=self.on_response,
            auto_ack=True)
        self.response = None
        self.corr_id = None


    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body

    def listFiles(self):
        self.response = None
        self.channel.basic_publish(
            exchange='',
            routing_key=self.config['request_queue'],
            properties=pika.BasicProperties(
                reply_to=self.config['response_queue'],
                correlation_id=self.corr_id
            ),
            body=str("list")
        )
        self.connection.process_data_events(time_limit=5)
        if self.response is None:
            raise Exception('No value returned')
        return (self.response)
    
    def findFiles(self, name):
        self.response = None
        self.channel.basic_publish(
            exchange='',
            routing_key=self.config['request_queue'],
            properties=pika.BasicProperties(
                reply_to=self.config['response_queue'],
                correlation_id=self.corr_id
            ),
            body=str(name)
        )
        self.connection.process_data_events(time_limit=5)
        if self.response is None:
            raise Exception('No value returned')
        return (self.response)

        
