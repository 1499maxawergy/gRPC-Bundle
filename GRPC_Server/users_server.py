import grpc
from concurrent import futures
import users_pb2 as pb2
import users_pb2_grpc as pb2_grpc
from clients import finder, updater, deleter, adder

class UserService(pb2_grpc.UserServiceServicer):

    def __init__(self, *args, **kwargs):
        pass

    def login(self, request, context):
        username = request.username
        password = request.password
        is_found = finder(username=username, password=password)
        if is_found > -1:
            result = 'Привет, ' + str(username)
            result = {'message': result, 'success': True}
        else:
            result = 'Ошибка входа'
            result = {'message': result, 'success': False}
        return pb2.UserResponse(**result)

    def register(self, request, context):
        username = request.username
        password = request.password
        is_success = adder(username=username, password=password)
        if is_success:
            result = 'Успешная регистрация для ' + str(username)
            result = {'message': result, 'success': True}
        else:
            result = 'Ошибка авторизации'
            result = {'message': result, 'success': False}
        return pb2.UserResponse(**result)

    def delete(self, request, context):
        username = request.username
        password = request.password
        is_success = deleter(username=username, password=password)
        if is_success:
            result = f'Успешное удаление пользователя - ' + str(username)
            result = {'message': result, 'success': True}
        else:
            result = 'Ошибка удаления'
            result = {'message': result, 'success': False}
        return pb2.UserResponse(**result)

    def update(self, request, context):
        old_username = request.old_username
        old_password = request.old_password
        new_username = request.new_username
        new_password = request.new_password
        is_success = updater(
            old_username=old_username,
            old_password=old_password,
            new_username=new_username,
            new_password=new_password)
        if is_success:
            result = f'Успешная замена данных, ' + str(new_username)
            result = {'message': result, 'success': True}
        else:
            result = 'Ошибка замены данных'
            result = {'message': result, 'success': False}
        return pb2.UserResponse(**result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    print('Starting Server. Listening on port 50051.')
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()