FROM ubuntu:20.04 AS builder
ARG DEBIAN_FRONTEND=noninteractive

# Linux packages
RUN rm -rf /var/lib/apt/lists/* && \
        apt-get -y update

RUN apt-get install -y --no-install-recommends \
        python3-pip \
        python3-dev  \
        libpq-dev \
        && \
    apt-get -y autoremove && \
    apt-get -y clean

# Python packages
RUN pip3 install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir \
		matplotlib \
		pandas \
		scipy \
		astropy \
        schedule \
        ptvsd