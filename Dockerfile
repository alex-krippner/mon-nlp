FROM python:3.11.3-slim

ENV GRPC_PORT=50051

RUN mkdir /protos
RUN mkdir /adapters
RUN mkdir /adapters/genproto
RUN mkdir /domain
RUN mkdir /server
# The protos are placed in the same directory as the generated protos in order to have correct import statements
COPY protos/monNlpService.proto /adapters/genproto/monNlpService.proto
COPY requirements.txt requirements.txt
COPY adapters/mon_nlp_service.py /adapters/mon_nlp_service.py
COPY adapters/spacy_text_analysis.py /adapters/spacy_text_analysis.py
COPY domain/ /domain/
COPY server/ /server/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download ja_core_news_sm
RUN python -m grpc_tools.protoc --proto_path=. --python_out=. --pyi_out=. --grpc_python_out=. adapters/genproto/monNlpService.proto

COPY app.py app.py
COPY setup.py setup.py
EXPOSE 50051
ENTRYPOINT [ "python", "setup.py", "--port", "${GRPC_PORT}" ]