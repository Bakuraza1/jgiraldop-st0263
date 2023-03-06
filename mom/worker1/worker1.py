import pika, os, glob, json

with open("/home/ubuntu/reto2/topicos_telematica_reto2/mom/worker1/config.json", "r") as jsonfile:
    config = json.load(jsonfile)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='rpc_request')

def listFiles():
    directory = "mom1 \n"
    path = config['dir_path']
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            directory += (os.path.join(root, name)) + "\n"
    return directory

def findFiles(name):
    name = str(name).replace('.','/')
    files = glob.glob(config['dir_path'] + name +"*.*")
    ans = ""
    if len(files) == 0:
        return 'mom1 \n no files found'
    else:
        ans += ('mom1 \n file(s) found:')
        ans +=('\n'.join(files))
        return ans

def on_request(ch, methods, props, body):
    param = ((body).decode("utf-8")) 
    if param == "list":
        response = listFiles()
    else:
        response = findFiles(param)
    channel.basic_publish(exchange='' ,
                          routing_key=props.reply_to,
                          properties=pika.BasicProperties(correlation_id=props.correlation_id),
                          body=str(response))
    channel.basic_ack(delivery_tag=methods.delivery_tag)

def run():  
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=config['queue'], on_message_callback=on_request)
    print("Waiting for RPC request")
    channel.start_consuming()


if __name__ == "__main__":
    run()

                                                          
    