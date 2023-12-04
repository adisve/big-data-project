from pyspark.sql import SparkSession
from spark.utils.wrappers import available


class Dataset(object):
    """
    Class to contain the dataset and perform processing on it, as well
    as provide access to the dataframes attributes.
    """

    def __init__(self, hdfs_path, spark_master):
        self._init_session(spark_master)
        self.hdfs_path = hdfs_path
        self._df = None

    def _init_session(self, spark_master):
        self.spark = (
            SparkSession.builder.master(spark_master)
            .appName("Reddit word analysis")
            .getOrCreate()
        )

    def pre_process(self):
        df = (
            self.spark.read.format("parquet")
            .option("header", "true")
            .load(self.hdfs_path)
        )
        df = df[["body", "score", "subreddit"]]
        df = df.filter(df.body != "[deleted]")
        df = df.filter(df.body != "[removed]")
        self._df = df

    @available
    def show(self):
        self._df.show()

    @property
    @available
    def schema(self):
        return self._df.schema

    @property
    @available
    def dataframe(self):
        return self._df
