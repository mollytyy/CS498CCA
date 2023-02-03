import json
import boto3

dynamodb = boto3.resource('dynamodb')
client = boto3.client('dynamodb')


def get_distance(source, destination):
    print('get_distance, source = ' + str(source) + ' to ' + str(destination))
    tableGraph = dynamodb.Table('Graph')
    response = tableGraph.get_item(
        Key={
            'source': source,
            'destination': destination
        }
    )
    print(response)
    return response['Item']['distance']


def lambda_handler(event, context):
    print('received request: ' + str(event))
    source_input = event['currentIntent']['slots']['source']
    destination_input = event['currentIntent']['slots']['destination']
    dist = get_distance(source_input, destination_input)
    response = {
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
                "contentType": "SSML",
                "content": dist
            },
        }
    }
    print('result = ' + str(response))
    return response
