import grpc
from . import users_pb2_grpc as pb2_grpc
from . import users_pb2 as pb2

class UserClient(object):

    def __init__(self):
        self.host = 'localhost'
        self.server_port = 50051

        self.channel = grpc.insecure_channel(
            '{}:{}'.format(self.host, self.server_port))

        self.stub = pb2_grpc.UserServiceStub(self.channel)
    
    def getLogin(self, username, password):
        message = pb2.UserData(username=username, password=password)
        return self.stub.login(message)

    def getRegister(self, username, password):
        message = pb2.UserData(username=username, password=password)
        return self.stub.register(message)

    def getDelete(self, username, password):
        message = pb2.UserData(username=username, password=password)
        return self.stub.delete(message)

    def getUpdate(self, old_username, old_password, new_username, new_password):
        message = pb2.UserDataUpdate(
            new_username=new_username,
            new_password=new_password,
            old_username=old_username,
            old_password=old_password
        )
        return self.stub.update(message)