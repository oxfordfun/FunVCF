From ubuntu:18.04

LABEL version = 0.1.0 \
      description='Fun VCF' \
      dockerhub='oxfordmmm/funvcf:v0.1.0'

RUN apt-get update && \
    apt-get install -y software-properties-common

RUN apt install -y \
    libbz2-dev \
    liblzma-dev \
    zlib1g-dev

RUN apt-get install python3-pip -y

RUN pip3 install pysam
RUN pip3 install vcfpy


#Build #docker build -t funvcf:v0.1.0 .
#Tag   #docker tag funvcf:v0.1.0 oxfordmmm/funvcf:v0.1.0
#Push  #docker push oxfordmmm/funvcf:v0.1.0
#Pull  #docker pull oxfordmmm/funvcf:v0.1.0
#Transform #singularity build funvcf-v0.1.0.img docker://oxfordmmm/funvcf:v0.1.0
