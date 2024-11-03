# Realtime Data Streaming | End-to-End Data Engineering Project

This project demonstrates a real-time data streaming architecture, designed for data ingestion, processing, and storage. It incorporates an API for data ingestion, Apache Airflow for workflow orchestration, Apache Kafka (with ZooKeeper for coordination) for data streaming, Apache Spark for distributed data processing, and Cassandra for data storage. The entire setup is containerized using Docker, enabling seamless deployment and scalability.

## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [Project Highlights](#project-highlights)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Configuration](#configuration)
- [Watch the Video Tutorial](#watch-the-video-tutorial)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project serves as a comprehensive guide to building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. Each component is containerized with Docker, making deployment and management straightforward.

## System Architecture

![System Architecture]([(https://github.com/vinibeni2801/proj-stack-e2e-stream-eng/blob/main/image/Untitled-2024-07-31-2232.png])

The architecture is structured as follows:

- **Data Source**: `random-data-api.com` API generates sample data for the pipeline.
- **Apache Airflow**: Manages and schedules the workflows, including fetching data and storing it in a PostgreSQL database.
- **Apache Kafka & ZooKeeper**: Kafka streams the data from PostgreSQL to downstream processing. ZooKeeper coordinates the Kafka brokers.
- **Control Center & Schema Registry**: Facilitates Kafka stream monitoring and schema management.
- **Apache Spark**: Processes data in a distributed fashion, with a setup of master and worker nodes.
- **Cassandra**: Serves as the primary data storage for processed data, ensuring high availability and scalability.

## Project Highlights

In this project, you will:

- Learn how to set up and orchestrate data pipelines with Apache Airflow.
- Stream real-time data efficiently using Apache Kafka and Zookeeper.
- Explore distributed data processing with Apache Spark.
- Understand best practices for data storage using Cassandra and PostgreSQL.
- Build, manage, and scale containerized applications using Docker.

## Technologies

The project leverages a variety of technologies:

- **Apache Airflow**: Workflow management and scheduling
- **Python**: General-purpose programming for pipeline scripts
- **Apache Kafka**: Data streaming and messaging
- **Apache Zookeeper**: Kafka broker coordination
- **Apache Spark**: Distributed data processing
- **Cassandra**: NoSQL database for storage
- **PostgreSQL**: Relational database for data ingestion
- **Docker**: Containerization and deployment

## Getting Started

Follow these steps to set up the project locally:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/vinibeni2801/proj-stack-e2e-stream-eng.git
    ```

2. **Navigate to the project directory:**
    ```bash
    cd proj-stack-e2e-stream-eng
    ```

3. **Build and start services with Docker Compose:**
    ```bash
    docker-compose up --build
    ```

4. **Verify Services**:
   - Access Apache Airflow at [http://localhost:8080](http://localhost:8080).
   - Access Kafka Control Center at [http://localhost:9021](http://localhost:9021).
   - Access Cassandra at [http://localhost:9042](http://localhost:9042) or via `cqlsh` for command-line access.

## Configuration

### Python Version
Ensure your Python version is between **3.8 and 3.12** for compatibility with project dependencies.

### Docker Resources
For smooth operation, Docker should have adequate resources allocated:
   - **Memory**: At least 4GB
   - **CPUs**: At least 2
   - **Disk Space**: 5GB or more
