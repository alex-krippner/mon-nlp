import grpc
from concurrent import futures
import monNlpService_pb2_grpc
import monNlpService_pb2
from mon_nlp import MonNlpService
import logging
from grpc_reflection.v1alpha import reflection

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  monNlpService_pb2_grpc.add_MonNlpServiceServicer_to_server(
     MonNlpService(), server)

  # Enable gRPC reflection
  SERVICE_NAMES = (
  monNlpService_pb2.DESCRIPTOR.services_by_name['MonNlpService'].full_name,
      # Add more service names if needed
  )
  reflection.enable_server_reflection(SERVICE_NAMES, server)     
  server.add_insecure_port('[::]:50051')
  logging.info("Starting server")
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()