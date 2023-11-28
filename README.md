# Big Data Project

## Project Description

This project is a part of the Big Data course at the Kristianstad University. The goal of the project is to create a data pipeline that can be used to analyze the data from the [May 2015 Reddit Comments Dataset](https://www.kaggle.com/datasets/kaggle/reddit-comments-may-2015/) available on Kaggle. The data pipeline is created using Apache Spark and Hadoop and the data is stored in HDFS as Parquet files. The data pipeline is run in a Docker cluster.

## Pre-requisites

- Docker
- Docker Compose
- Python 3.11.6
- Pipenv

## How to run

1. Clone the repository

2. Follow the instructions in [this repository](https://github.com/adisve/hadoop-spark-cluster) in order to accurately setup a Hadoop/Spark cluster.

3. Navigate to the project root

4. Enter the jupyter-notebook directory and run the following command to start the Jupyter Notebook server:

```bash
docker-compose up -d
```

The Jupyter notebook server is now running on port 8888, without token authentication.

## Authors

- [Adis Veletanlic](https://github.com/adisve)
- [Dzenis Madzovic](https://github.com/psychicplatypus)
