from typing import Dict, List, Type
import logging
from concurrent import futures
import grpc
from grpc_reflection.v1alpha import reflection


class Server:
    """A class creating a grpc server"""

    def __init__(self, services: List[Dict[str, Type]]):
        self.services = services

    def __add_services(self, server: grpc.Server) -> List[str]:
        service_names = []
        for service in self.services:
            service_pb = service["pb"]
            service_name = service["name"]
            service_pb_grpc = service["pb_grpc"]
            service_implementation = service["implementation"]

            getattr(service_pb_grpc, f"add_{service_name}Servicer_to_server")(
                service_implementation, server
            )

            service_names.extend(
                [service_pb.DESCRIPTOR.services_by_name[service_name].full_name]
            )

        logging.info(f"Services added to grpc server: {', '.join(service_names)}")
        return service_names

    def start(self):
        """Creates, registers, and starts server"""
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        service_names = self.__add_services(server)

        reflection.enable_server_reflection(service_names, server)
        server.add_insecure_port("[::]:50051")
        logging.info("Starting server")
        server.start()
        server.wait_for_termination()
