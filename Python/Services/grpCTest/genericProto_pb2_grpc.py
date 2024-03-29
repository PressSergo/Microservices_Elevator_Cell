# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import genericProto_pb2 as genericProto__pb2


class DataHashStub(object):
    """Missing associated documentation comment in .proto file"""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.hash_md5 = channel.unary_unary(
                '/DataHash/hash_md5',
                request_serializer=genericProto__pb2.Text.SerializeToString,
                response_deserializer=genericProto__pb2.Text.FromString,
                )
        self.hash_sha256 = channel.unary_unary(
                '/DataHash/hash_sha256',
                request_serializer=genericProto__pb2.Text.SerializeToString,
                response_deserializer=genericProto__pb2.Text.FromString,
                )


class DataHashServicer(object):
    """Missing associated documentation comment in .proto file"""

    def hash_md5(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def hash_sha256(self, request, context):
        """Missing associated documentation comment in .proto file"""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataHashServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'hash_md5': grpc.unary_unary_rpc_method_handler(
                    servicer.hash_md5,
                    request_deserializer=genericProto__pb2.Text.FromString,
                    response_serializer=genericProto__pb2.Text.SerializeToString,
            ),
            'hash_sha256': grpc.unary_unary_rpc_method_handler(
                    servicer.hash_sha256,
                    request_deserializer=genericProto__pb2.Text.FromString,
                    response_serializer=genericProto__pb2.Text.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DataHash', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DataHash(object):
    """Missing associated documentation comment in .proto file"""

    @staticmethod
    def hash_md5(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataHash/hash_md5',
            genericProto__pb2.Text.SerializeToString,
            genericProto__pb2.Text.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def hash_sha256(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DataHash/hash_sha256',
            genericProto__pb2.Text.SerializeToString,
            genericProto__pb2.Text.FromString,
            options, channel_credentials,
            call_credentials, compression, wait_for_ready, timeout, metadata)
