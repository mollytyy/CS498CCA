from pyspark.ml.classification import RandomForestClassifier
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import StringIndexer
import numpy as np

sc = SparkContext()
sqlContext = SQLContext(sc)


def predict(df_train, df_test):
    # Train random forest classifier

    # Hint: Column names in the given dataframes need to match the column names
    # expected by the random forest classifier `train` and `transform` functions.
    # Or you can alternatively specify which columns the `train` and `transform`
    # functions should use
    label_stringIdx = StringIndexer(inputCol="label", outputCol="indexed")
    df_train = label_stringIdx.fit(df_train).transform(df_train)
    rf = RandomForestClassifier(labelCol='indexed', featuresCol='features')
    model = rf.fit(df_train)
    predictions = model.transform(df_test)
    result = predictions.select('prediction').collect()
    re = []
    for r in result:
        re.append(r.prediction)
    # Result: Result should be a list with the trained model's predictions
    # for all the test data points
    return re


def main():
    raw_training_data = sc.textFile("dataset/training.data")

    # Convert text file into an RDD which can be converted to a DataFrame
    # Hint: For types and format look at what the format required by the
    # `train` method for the random forest classifier
    # Hint 2: Look at the imports above
    rdd_train = raw_training_data.map(lambda x: x.rsplit(',', 1)).map(lambda x: (int(x[1]), Vectors.dense([float(x) for x in x[0].split(',')])))

    # Create dataframe from the RDD
    df_train = sqlContext.createDataFrame(rdd_train, ['label', 'features'])
    
    raw_test_data = sc.textFile("dataset/test-features.data")

    # Convert text file lines into an RDD we can use later
    rdd_test = raw_test_data.map(lambda x: [Vectors.dense([float(x) for x in x.split(',')]).tolist()])
    # rdd_test = raw_test_data.map(lambda x: ([float(i) for i in x.split(',')])).map(lambda x: Vectors.dense([x]).tolist())
    # rdd_test = raw_test_data.map(lambda x: ([float(i) for i in x.split(',')])).map(lambda x: Vectors.dense(x))
    # rdd_test = raw_test_data.map(lambda x: ([float(i) for i in x.split(',')])).map(lambda x: Vectors.dense(x))
    # rdd_test = raw_test_data.map(lambda x: Vectors.dense([float(i) for i in x.split(',')]))
    rdd_test = raw_test_data.map(lambda x: Vectors.dense([float(i) for i in x.split(',')])).map(lambda v: [(Vectors.dense(v))])
    # rdd_test = raw_test_data.map(lambda x: Vectors.sparse(len(x.split(',')), range(len(x.split(','))), [float(i) for i in x.split(',')]))


    
    # Create dataframe from RDD
    df_test = sqlContext.createDataFrame(rdd_test, ['features'])

    predictions = predict(df_train, df_test)

    # You can take a look at dataset/test-labels.data to see if your
    # predictions were right
    for pred in predictions:
        print(int(pred))


if __name__ == "__main__":
    main()
