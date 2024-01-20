## Build

`./build.sh <container_tag>`  

For example: ./build.sh mon_nlp

## Run

`./run.sh <container_tag>`  

For example: ./build.sh mon_nlp

## Test grpc without docker

`grpcurl -plaintext -d '{"text": "石川県で確認された 死者126人に　能登半島地震"}' localhost:50051 monNlp.MonNlpService/tokenize`

## Test grpc running in docker container

`grpcurl -plaintext -d '{"text": "石川県で確認された 死者126人に　能登半島地震"}' mon_nlp_server:50051 monNlp.MonNlpService/tokenize`
