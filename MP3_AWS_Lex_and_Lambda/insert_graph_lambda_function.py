import json
import boto3

from collections import defaultdict


dynamo = boto3.resource('dynamodb')


def lambda_handler(event, context):
    # Instanciating connection objects with DynamoDB using boto3 dependency
    dynamo = boto3.resource('dynamodb')
    client = boto3.client('dynamodb')

    # getting the table
    tableGraph = dynamo.Table('Graph')

    # Clear the table so there are no stale items
    truncateTable(tableGraph)

    # recieve HTTP POST graph
    json_string = event['graph']

    # parse json
    graph, places = parse_json(json_string)

    # make all combination
    places_list = []
    for i in range(len(places)):
        for j in range(len(places)):
            places_list.append([i, j])

    # run bfs
    put_list = []
    for p in places_list:
        item = {}
        item['source'] = places[p[0]]
        item['destination'] = places[p[1]]
        item['distance'] = bfs(graph, places[p[0]], places[p[1]])
        put_list.append(item)
    print(put_list)

    # try/catch to add data into dynamo
    try:
        with tableGraph.batch_writer() as batch:
            for put in put_list:
                batch.put_item(put)

        return {
            'statusCode': 200,
            'body': json.dumps('Successfully inserted the graph!')
        }
    except:
        print('Closing lambda function')
        return {
            'statusCode': 400,
            'body': json.dumps('Error saving the graph')
        }


def truncateTable(table):
    # table = dynamo.Table(table)
    scan = table.scan()
    with table.batch_writer() as batch:
        for each in scan['Items']:
            batch.delete_item(
                Key={
                    'source': each['source'],
                    'destination': each['destination']
                }
            )


def parse_json(json_string):
    graph = defaultdict(list)
    edges = json_string.split(',')
    places = set()
    for edge in edges:
        source, destination = edge.split('->')
        graph[source].append(destination)
        places.add(source)
        places.add(destination)
    return graph, list(places)


def bfs(graph, start, end):
    visited = set()
    queue = [(start, 0)]
    while queue:
        node, distance = queue.pop(0)
        if node == end:
            return distance
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, distance + 1))
    return -1
