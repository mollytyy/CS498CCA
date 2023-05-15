# Fetch ubuntu 22.04 LTS docker image
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND noninteractive

RUN \
  apt-get update && \
  apt-get install -y --no-install-recommends net-tools vim sudo expect ssh openssh-server zip unzip wget openjdk-11-jdk gcc \
  python3-pip python3-dev python3-setuptools && \
  apt-get autoremove -qq -y --purge && \
  apt-get clean && \
  rm -rf /var/cache/apt /var/lib/apt/lists && \
  cd /usr/local/ && \
  wget "https://archive.apache.org/dist/zookeeper/zookeeper-3.4.13/zookeeper-3.4.13.tar.gz" &&\
  tar -xvf zookeeper-3.4.13.tar.gz && \
  ln -s ./zookeeper-3.4.13 zookeeper &&  \
  rm -rf /usr/local/zookeeper-3.4.13.tar.gz && \
  mkdir /usr/local/zookeeper/data && \
  mkdir /usr/local/zookeeper/log && \
  rm -rf /usr/local/zookeeper/docs && \
  bash -c "echo '1' >> /usr/local/zookeeper/data/myid" && \
  chmod a+rwx -R /usr/local/zookeeper/ && \
  wget "https://archive.apache.org/dist/hbase/2.4.16/hbase-2.4.16-bin.tar.gz" && \
  tar -xzf hbase-2.4.16-bin.tar.gz && \
  rm -rf /usr/local/hbase-2.4.16-bin.tar.gz && \
  mv /usr/local/hbase-2.4.16* /usr/local/hbase && \
  rm -rf /usr/local/hbase/docs && \
  chmod a+rwx -R /usr/local/hbase/ && \
  pip3 install wheel happybase && \
  cd /usr/local/ && \
  wget "https://archive.apache.org/dist/phoenix/phoenix-5.1.3/phoenix-hbase-2.4.0-5.1.3-bin.tar.gz" && \
  tar -xzf phoenix-hbase-2.4.0-5.1.3-bin.tar.gz && \
  rm -rf /usr/local/phoenix-hbase-2.4.0-5.1.3-bin.tar.gz && \
  mv /usr/local/phoenix-hbase-2.4.0-5.1.3* /usr/local/phoenix && \
  rm -rf /usr/local/phoenix/docs && \
  chmod a+rwx -R /usr/local/phoenix/ && \
  cp /usr/local/phoenix/phoenix-server-hbase-2.4.0-5.1.3.jar /usr/local/hbase/lib/

RUN cd /usr/local/bin; \
  ln -s /usr/bin/python3 python; 

ENV CLASSPATH=$CLASSPATH:/usr/local/phoenix/phoenix-client-hbase-2.4.0-5.1.3.jar

COPY zoo.cfg /usr/local/zookeeper/conf/zoo.cfg
COPY hbase-site.xml /usr/local/hbase/conf/hbase-site.xml
COPY hbase-env.sh /usr/local/hbase/conf/hbase-env.sh

COPY auto* /usr/local/bin/
RUN chmod 777 /usr/local/bin/auto*
RUN adduser hadoopuser --disabled-password --gecos ""
RUN echo 'hadoopuser:hadooppass' | chpasswd && usermod -aG sudo hadoopuser
RUN sh -c "echo 'hadoopuser ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers"

ENV HBASE_HOME /usr/local/hbase
ENV PATH="/usr/local/hbase/bin:${PATH}"
ENV PATH="/usr/local/zookeeper/bin:${PATH}"
RUN chmod a+rwx -R /usr/local/hbase/


# Make vim nice
RUN echo "set background=dark" >> ~/.vimrc

