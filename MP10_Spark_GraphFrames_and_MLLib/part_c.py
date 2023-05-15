from pyspark import *
from pyspark.sql import SparkSession
from graphframes import *

sc = SparkContext()
spark = SparkSession.builder.appName('fun').getOrCreate()


def get_shortest_distances(graphframe, dst_id):
    # Find shortest distances in the given graphframe to the vertex which has id `dst_id`
    # The result is a dictionary where key is a vertex id and the corresponding value is
    # the distance of this node to vertex `dst_id`.
    re = {}
    for i in range(graphframe.vertices.count()):
        result = graphframe.bfs(fromExpr=f"id = {i}", toExpr=f"id = {dst_id}")
        result = result.select("*").collect()
        if len(result) > 0:
            c = 0
            for j in result:
                d = j.asDict()
                while 'e' + str(c) in d.keys():
                    c += 1
            re[i] = c
        else:
            re[i] = -1
    return re

if __name__ == "__main__":
    vertex_list = []
    edge_list = []
    with open('dataset/graph.data') as f:
        for line in f:
            parsed = line.strip().split(' ')
            src = parsed[0]  # Parse src from line
            dst_list = []  # Parse dst_list from line
            dst_list.extend(parsed[1:])
            vertex_list.append((src,))
            edge_list += [(src, dst) for dst in dst_list]

    vertices = spark.createDataFrame(vertex_list, ['id'])  # Create vertices dataframe
    edges = spark.createDataFrame(edge_list, ['src', 'dst'])  # Create edges dataframe
    
    g = GraphFrame(vertices, edges)
    sc.setCheckpointDir("/tmp/shortest-paths")

    # We want the shortest distance from every vertex to vertex 1
    for k, v in get_shortest_distances(g, '1').items():
        print(k, v)
