import adapters.genproto.monNlpService_pb2_grpc
import adapters.genproto.monNlpService_pb2
from domain.text_analysis import TextAnalyzer


class MonNlpService(adapters.genproto.monNlpService_pb2_grpc.MonNlpServiceServicer):
    def __init__(self, text_analyzer: TextAnalyzer):
        self.text_analyzer = text_analyzer

    def tokenize(self, request, context):
        entities = self.text_analyzer.analyze_text(request.text)
        tokens = []
        for entity in entities:
            tokens.append(entity["text"])
        response = adapters.genproto.monNlpService_pb2.TokenizeResponse(tokens=tokens)
        return response
