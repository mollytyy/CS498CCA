from kubernetes import client, config
from flask import Flask, request
from os import path
import yaml
import random
import string
import json
import sys
import json

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()
v1 = client.CoreV1Api()
batch_v1 = client.BatchV1Api()
app = Flask(__name__)
# app.run(debug = True)


@app.route('/config', methods=['GET'])
def get_config():
    pods = []

    list_pod = v1.list_pod_for_all_namespaces().items

    for pod in list_pod:
        d = {
            "name": pod.metadata.name,
            "ip": pod.status.pod_ip,
            "namespace": pod.metadata.namespace,
            "node": pod.spec.node_name,
            "status": pod.status.phase
        }
        pods.append(d)

    output = {"pods": pods}
    output = json.dumps(output)

    return output


@app.route('/img-classification/free', methods=['POST'])
def post_free():
    free = open("free-job.yaml")
    job = yaml.safe_load(free)

    api_response = batch_v1.create_namespaced_job(
        body=job, namespace="free-service")

    return "success"


@app.route('/img-classification/premium', methods=['POST'])
def post_premium():
    premium = open("premium-job.yaml")
    job = yaml.safe_load(premium)

    api_response = batch_v1.create_namespaced_job(
        body=job, namespace="default")

    return "success"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
