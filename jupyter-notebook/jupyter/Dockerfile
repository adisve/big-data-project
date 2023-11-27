FROM jupyter/datascience-notebook

USER root

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean;

ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64

RUN chown -R jovyan:users /home/jovyan

USER jovyan

RUN pip install pyspark pandas matplotlib torch scikit-learn