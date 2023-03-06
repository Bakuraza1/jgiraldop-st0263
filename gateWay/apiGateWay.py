import grpc, json
from flask import Flask, redirect
from grpc_config.files_pb2_grpc import getFilesStub
from grpc_config.files_pb2 import Nulo, Files
from testClientMOM import testRpcClient

rpc = True
app = Flask(__name__)
mom_request_files = testRpcClient()
with open("/home/ubuntu/jgiraldop-st0263/gateWay/config.json", "r") as jsonfile:
    config = json.load(jsonfile)


def balance():
    global rpc
    if rpc:
        rpc = not rpc
    else:
        rpc = not rpc
    return rpc


@app.route('/')
def alive():
    return('Alive')


@app.route('/listFiles')
def listFiles():
    balance()
    if rpc:
        try:
            with grpc.insecure_channel(config['rpc_address']+':'+config['rpc_port']) as channel1:
                stub = getFilesStub(channel1)
                request = Nulo()
                response = stub.ListFiles(request)
                return response.Files
        except:
            return redirect("/listFiles")
    else:
        try:
            response = mom_request_files.listFiles()
            return response
        except:
            return redirect("/listFiles")


@app.route('/getFile/<string:name>')
def getFile(name):
    balance()
    if rpc:
        try:
            with grpc.insecure_channel(config['rpc_address']+':'+config['rpc_port']) as channel1:
                stub = getFilesStub(channel1)
                request = Files(Files=name)
                response = stub.FindFiles(request)
                return response.Files
        except:
            return redirect("/getFile/"+name)
    else:
        try:
            response = mom_request_files.findFiles(name)
            return response
        except:
            return redirect("/getFile/"+name)
 

    


@app.route('/getFileRPC/<string:name>')
def getFileRPC(name):
    try:
        with grpc.insecure_channel(config['rpc_address']+':'+config['rpc_port']) as channel1:
            stub = getFilesStub(channel1)
            request = Files(Files=name)
            response = stub.FindFiles(request)
            return response.Files
    except:
        return("Time out")


@app.route('/getFileMOM/<string:name>')
def getFileMOM(name):
    response = mom_request_files.findFiles(name)
    return response



@app.route('/testRPC')
def testRPC():
    try:
        with grpc.insecure_channel(config['rpc_address']+':'+config['rpc_port']) as channel1:
            stub = getFilesStub(channel1)
            request = Nulo()
            response = stub.ListFiles(request)
            return response.Files
    except:
        return("Time out")


@app.route('/textMOM')
def testMOM():
    response = mom_request_files.listFiles()
    return response


if __name__ == "__main__":
    app.run(host=config['server_address'], port=config['server_port'])