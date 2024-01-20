#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide tag of the Docker image"
    exit 1
fi

readonly tag="$1"

docker run --name mon_nlp_server --network backend_default -p 50051:50051 -e GRPC_PORT=50051 --rm "$tag"