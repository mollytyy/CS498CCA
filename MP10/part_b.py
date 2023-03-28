from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors
import pyspark.sql.functions as F

############################################
#### PLEASE USE THE GIVEN PARAMETERS     ###
#### FOR TRAINING YOUR KMEANS CLUSTERING ###
#### MODEL                               ###
############################################

NUM_CLUSTERS = 4
SEED = 0
MAX_ITERATIONS = 100
INITIALIZATION_MODE = "random"

sc = SparkContext()
sqlContext = SQLContext(sc)


def get_clusters(df, num_clusters, max_iterations, initialization_mode,
                 seed):
    # Use the given data and the cluster pparameters to train a K-Means model
    # Find the cluster id corresponding to data point (a car)
    # Return a list of lists of the titles which belong to the same cluster
    # For example, if the output is [["Mercedes", "Audi"], ["Honda", "Hyundai"]]
    # Then "Mercedes" and "Audi" should have the same cluster id, and "Honda" and
    # "Hyundai" should have the same cluster id
    kmeans = KMeans(featuresCol='features', k=num_clusters, maxIter=max_iterations, initMode=initialization_mode).setSeed(seed)
    model = kmeans.fit(df)
    transformed = model.transform(df).select('id', 'prediction')
    rows = transformed.collect()
    comp = {}
    for i in range(len(rows)):
        if rows[i]['prediction'] in comp.keys():
            comp[rows[i]['prediction']].append(rows[i]['id'])
        else:
            comp[rows[i]['prediction']] = [rows[i]['id']]
    return comp.values()


def parse_line(line):
    # Parse data from line into an RDD
    # Hint: Look at the data format and columns required by the KMeans fit and
    # transform functions
    line = line.split(',', 1)
    re = []
    re.append(str(line[0]))
    sub = []
    for l in line[1].split(','):
        sub.append(float(l))
    re.append(Vectors.dense(sub))
    print(re)
    return re


if __name__ == "__main__":
    f = sc.textFile("dataset/cars.data")

    rdd = f.map(parse_line)
    # Convert RDD into a dataframe
    df = sqlContext.createDataFrame(rdd, ['id', 'features'])

    clusters = get_clusters(df, NUM_CLUSTERS, MAX_ITERATIONS,
                            INITIALIZATION_MODE, SEED)
    for cluster in clusters:
        print(','.join(cluster))
