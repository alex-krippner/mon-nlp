FROM python:3.11.3-slim

ENV GRPC_PORT=50051

RUN mkdir /services
RUN mkdir /protos
COPY protos/ /protos/
COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python -m spacy download ja_core_news_sm
RUN python3 -m grpc_tools.protoc -I ./protos --python_out=. \
           --pyi_out=. \
           --grpc_python_out=. ./protos/monNlpService.proto

COPY app.py app.py
COPY mon_nlp.py mon_nlp.py
EXPOSE 50051
ENTRYPOINT [ "python", "app.py", "--port", "${GRPC_PORT}" ]