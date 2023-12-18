#!/bin/bash

docker run --name mon_nlp_server --network backend_default -p 50051:50051 -e GRPC_PORT=50051 --rm test-spacy