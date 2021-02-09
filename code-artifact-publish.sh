#!/bin/bash
#
# Manual build, setup, publish to CodeArtifact

if [ -z "$CODE_ARTIFACT_OWNER" ] ||  [ -z "$CODE_ARTIFACT_DOMAIN" ] || [ -z "$CODE_ARTIFACT_REPO" ] 
then
    echo "Environment variables CODE_ARTIFACT_OWNER, CODE_ARTIFACT_DOMAIN, and CODE_ARTIFACT_REPO must be set prior to running this script."
    exit 1
fi

aws codeartifact login \
    --tool twine \
    --repository $CODE_ARTIFACT_REPO \
    --domain $CODE_ARTIFACT_DOMAIN \
    --domain-owner $CODE_ARTIFACT_OWNER

python3 setup.py sdist # bdist_wheel
twine upload --verbose --skip-existing --repository codeartifact dist/*
