import adapters.genproto.monNlpService_pb2
import adapters.genproto.monNlpService_pb2_grpc
from adapters.mon_nlp_service import MonNlpService
from adapters.spacy_text_analysis import SpacyTextAnalysis
from domain.text_analysis import TextAnalyzer
from server.server import Server


class App:
    """A class responsible for preparing the application for start up"""

    def __init__(self) -> None:
        self.nlp_processor = SpacyTextAnalysis()
        self.text_analyzer = TextAnalyzer(self.nlp_processor)

    def __prepare_server(self):
        services = [
            {
                "name": "MonNlpService",
                "pb": adapters.genproto.monNlpService_pb2,
                "pb_grpc": adapters.genproto.monNlpService_pb2_grpc,
                "implementation": MonNlpService(self.text_analyzer),
            }
        ]

        server = Server(services)
        return server

    def start(self):
        server = self.__prepare_server()
        server.start()
