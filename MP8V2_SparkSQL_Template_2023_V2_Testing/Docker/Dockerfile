# Fetch ubuntu 22.04 LTS docker image
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND noninteractive
ENV PYSPARK_PYTHON=python3

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential\
	expect git vim zip unzip wget openjdk-8-jdk wget maven sudo curl
RUN apt-get install -y python3 python3-pip


################################################################################
####################   Spark stuff   ###########################################
################################################################################

# Download and install spark
RUN curl -s "https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.tgz" | tar -xz  -C /usr/local/ \
    && ln -s /usr/local/spark-3.3.2-bin-hadoop3 /usr/local/spark \
    && chmod a+rwx -R /usr/local/spark/

RUN pip3 install --upgrade pip
RUN pip3 install Cython
RUN pip3 install numpy

RUN echo "alias spark-submit='/usr/local/spark/bin/spark-submit'" >> ~/.bashrc

# Ensure spark log output is redirected to stderr
RUN cp /usr/local/spark/conf/log4j2.properties.template /usr/local/spark/conf/log4j2.properties

# Set relevant environment variables to simplify usage of spark
ENV SPARK_HOME /usr/local/spark
ENV PATH="/usr/local/spark/bin:${PATH}"
RUN chmod a+rwx -R /usr/local/spark/

# Test the arch and set JAVA_HOME accordingly:
# ARM64: /usr/lib/jvm/java-8-openjdk-arm64
# X84_64: /usr/lib/jvm/java-1.8.0-openjdk-amd64

RUN if [ "$(uname -m)" = "x86_64" ]; then export JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-amd64; else export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64; fi \
    && echo "export JAVA_HOME=$JAVA_HOME" >> /root/.bashrc

RUN if [ "$(uname -m)" = "x86_64" ]; then update-java-alternatives --set java-1.8.0-openjdk-amd64; else update-java-alternatives --set java-1.8.0-openjdk-arm64; fi

# [Optional] Set working path to /cs498, and run the following command to start the container with code:
# WORKDIR /cs498
# docker run -it --rm --mount type=bind,source=$PATH_TO_CODE,target=/cs498/ sample_image.v1 /bin/bash
