#!/bin/bash

# V2

# docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate \
#     --input-spec https://developer.cloudcheckr.com/us/CloudCheckrApi.json \
#     --lang python \
#     --config /local/swag.config.python.json \
#     --output /local/out/python

# docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli help generate

# docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli config-help -l python

#V3

# docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3:3.0.24 generate --help

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli-v3:3.0.24 generate \
    --input-spec https://developer.cloudcheckr.com/us/CloudCheckrApi.json \
    --lang python \
    --config /local/swag.config.python.json \
    --output /local/out/python \
    --git-user-id CU-CommunityApps \
    --git-repo-id ct-cloudcheckr-cmx-client

