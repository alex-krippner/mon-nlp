#!/bin/bash

if [ -z "$1" ]; then
    echo "Please provide a tag for the Docker image"
    exit 1
fi

readonly tag="$1"
docker build -t "$tag" .