FROM jupyter/datascience-notebook

USER root

RUN apt-get update && \
    apt-get install -y openjdk-11-jdk && \
    apt-get clean;

RUN if [ "$(uname -m)" = "x86_64" ]; then \
        export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64; \
    elif [ "$(uname -m)" = "aarch64" ]; then \
        export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64; \
    fi

RUN chown -R jovyan:users /home/jovyan

USER jovyan

RUN pip install pyspark pandas matplotlib torch scikit-learn