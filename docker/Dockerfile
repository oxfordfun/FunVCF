From ubuntu:18.04

LABEL version = 0.1.0 \
      description='VCF Fun' \
      dockerhub='oxfordmmm/vcffun:v0.1.0'

RUN apt-get update && \
    apt-get install -y software-properties-common

RUN apt install -y \
    apt install libbz2-dev
    apt install liblzma-dev

RUN pip3 install pysam
RUN pip3 install vcfpy

