import org.apache.spark.SparkConf;
import org.apache.spark.api.java.JavaRDD;
import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.*;
import org.apache.spark.sql.types.DataTypes;
import org.apache.spark.sql.types.StructField;
import org.apache.spark.sql.types.StructType;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import org.apache.spark.api.java.function.Function;
import org.apache.spark.sql.expressions.Window;
import org.apache.spark.sql.expressions.WindowSpec;
import static org.apache.spark.sql.functions.*;

public class MP8_PartF {
    public static void main(String[] args) throws IOException {
        SparkSession spark = SparkSession
        .builder()
        .appName("MP8")
        .getOrCreate();
        JavaSparkContext sc = new JavaSparkContext(spark.sparkContext());
        SQLContext sqlContext = new SQLContext(sc);
        /*
        * 1. Setup: write a function to load it in an RDD & DataFrame
        */
        
        // RDD API
        // Columns: 0: word (string), 1: year (int), 2: frequency (int), 3: books (int)


        /**
         * 2. Frequency Increase (16 points): analyze the frequency increase of words starting from the year 1500 to the year 2000
         */
        
    }
}