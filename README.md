# data_pipeline_project

A data pipeline with Docker, Airflow, Kafka, Spark Streaming, cassandra

## Description

### Objective
The project is a streaming data pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra.Everything is containerized using Docker for ease of deployment and scalability.

### Tools & Technologies
- Containerization - [**Docker**](https://www.docker.com), [**Docker Compose**](https://docs.docker.com/compose/)
- Stream Processing - [**Kafka**](https://kafka.apache.org), [**Spark Streaming**](https://spark.apache.org/docs/latest/streaming-programming-guide.html)
- Orchestration - [**Airflow**](https://airflow.apache.org)
- Language - [**Python**](https://www.python.org)
- Data Warehouse - [**cassandra**](https://cassandra.apache.org/_/index.html)

### Architecture
![data_pipeline_project-architecture](https://github.com/mahesh-c-pathak/data_pipeline_project/blob/main/images/System%20Architecture.JPG)

The diagram above provides a detailed insight into pipeline's architecture. 

All applications are containerized into **Docker** containers.

**Data ingestion layer** - Python library Faker is used that generate synthetic data for testing, development, and analysis purposes. It provides a range of methods to generate realistic fake data, such as names, addresses, phone numbers, email addresses, dates, and more

**Orchestration layer** - Apache Airflow responsible for orchestrating the pipeline.

**Message broker layer** - messages from Producer are consumed by **Kafka** broker. The **Zookeeper** is launched before Kafka as it is required for its metadata management.Control Center and Schema Registry helps in monitoring and schema management of our Kafka streams.

**Stream processing layer** - For data processing with its master and worker nodes

**Serving database layer** - a **Cassandra** database stores & persists data from Spark jobs.





