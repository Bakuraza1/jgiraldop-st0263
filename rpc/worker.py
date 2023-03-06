import grpc, os, glob, json
from concurrent import futures
from grpc_config.files_pb2_grpc import getFilesServicer, add_getFilesServicer_to_server
from grpc_config.files_pb2 import Files

with open("/home/ubuntu/jgiraldop-st0263/rpc/config.json", "r") as jsonfile:
    config = json.load(jsonfile)

class getFileService(getFilesServicer):

    def Ready(self, request, context):
        return request
    
    def ListFiles(self, request, context):
        directory = "rpc \n"
        path = config["dir_path"]
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                directory += (os.path.join(root, name)) + "\n"
        return Files(Files=directory)
    
    def FindFiles(self, request, context):
        name = request.Files.replace('.','/')
        files = glob.glob(config['dir_path'] + name +"*.*")
        ans = "rpc \n"
        if len(files) == 0:
            return Files(Files='rpc \n no files found')
        else:
            ans += ('file(s) found:')
            ans += ('\n'.join(files))
            return Files(Files=ans)
    
    
def start():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    add_getFilesServicer_to_server(getFileService(), server)

    server.add_insecure_port('[::]:'+config['rpc_port'])
    print('server running on port 50051')

    server.start()

    server.wait_for_termination()


if __name__ == "__main__":
    start()