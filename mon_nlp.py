import monNlpService_pb2_grpc
import monNlpService_pb2
import logging

class MonNlpService(monNlpService_pb2_grpc.MonNlpServiceServicer):
    def tokenize(self, request, context):
        logging.info(request)
        response = monNlpService_pb2.TokenizeResponse()
        return response
