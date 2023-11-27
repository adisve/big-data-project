from pyspark.sql import SparkSession

class PreProcess(object):
    def __init__(self, hdfs_path, spark_master):
        # Connect to the Spark master running in Docker
        self.spark = SparkSession.builder \
            .master(spark_master) \
            .appName("Pre-processing Reddit Comments") \
            .getOrCreate()
        self.hdfs_path = hdfs_path
        self.df = None

    def run(self):
        df = self.spark.read.format("parquet").option("header", "true").load(self.hdfs_path)
        df = df.drop("downs", "ups", "subreddit")
        df = df.filter(df.body != "[deleted]")
        df = df.filter(df.body != "[removed]")
        self.df = df

    def show(self):
        self.df.show()
