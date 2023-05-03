FROM python:3.6

# Creating Application Source Code Directory
# RUN cat <<EOF | sudo tee /etc/yum.repos.d/kubernetes.repo
# [kubernetes]
# name=Kubernetes
# baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-\$basearch
# enabled=1
# gpgcheck=1
# gpgkey=https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
# EOF
# RUN sudo yum install -y kubectl
# RUN sudo yum install -y python36 python36-pip

# Setting Home Directory for containers
WORKDIR /mp12

# Installing python dependencies
# copy current files to src folder (requirements.txt and classify.py)
COPY requirements.txt requirements.txt
COPY classify.py classify.py

# install dependencies mentioned in requirements.txt
RUN pip3 install -r requirements.txt

# Application Environment variables. 
# These variables will be used when you run the image. 
# You will also need to pass corresponding DATASET and TYPE variables from the job yaml files of both free-service and default types of jobs.
ENV APP_ENV development
ENV DATASET mnist
ENV TYPE ff

# Exposing Ports
EXPOSE 5035

# Setting Persistent data
VOLUME ["/app-data"]

# Running Python Application (classify.py)
CMD ["python3", "-m", "classify"]
