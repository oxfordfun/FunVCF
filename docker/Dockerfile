From ubuntu:18.04

LABEL version = 0.1.0 \
      description='VCF Fun' \
      dockerhub='oxfordmmm/vcffun:v0.1.0'

RUN apt-get update && \
    apt-get install -y software-properties-common

RUN apt install -y \
    libbz2-dev \
    liblzma-dev \
    zlib1g-dev

RUN apt-get install python3-pip -y

RUN pip3 install pysam
RUN pip3 install vcfpy


#To build #docker build -t funvcf:v0.1.0 .
