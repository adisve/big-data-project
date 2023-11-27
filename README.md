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

4. Create a python virtual environment
```sh
pipenv install
```
5. Source the virtual environment
```sh
pipenv shell
```

6. 
