import grpc

import genericProto_pb2
import genericProto_pb2_grpc

# открываем канал и создаем клиент
channel = grpc.insecure_channel('localhost:6066')
stub = genericProto_pb2_grpc.DataHashStub(channel)

while True :
    text = str(input("message: "))
    # запрос за md5
    to_md5 = genericProto_pb2.Text(data=text)
    response = stub.hash_md5(to_md5)
    print(response.data)

    # запрос за ha256
    to_sha256 = genericProto_pb2.Text(data=text)
    response = stub.hash_sha256(to_sha256)
    print(response.data)