
# Real-Time E-Commerce Analytics Dashboard

## Overview

This project demonstrates the creation of a **real-time e-commerce analytics dashboard** using a robust tech stack including JAVA8, Apache Kafka, Spark Streaming, MySQL, InfluxDB, and Grafana. The dashboard provides key insights into user interactions, such as campaign performance, demographic trends, and real-time purchase analytics.

Time-series metrics form the backbone of this project, offering a powerful way to capture and analyze data that evolves over time.

---

## Key Features

- **Real-Time Data Processing**: Ingest and process live user events such as clicks and purchases.
- **Batch and Streaming Integration**: Combine demographic data with real-time purchase events.
- **Interactive Dashboard**: Visualize KPIs and insights with Grafana.
- **Time-Series Database**: Leverage InfluxDB for optimized storage and retrieval of time-series data.

---

## Tech Stack

- **Programming Languages**: Java 8, SQL
- **Services**:
  - Apache Kafka
  - Spark Streaming
  - MySQL
  - InfluxDB
  - Grafana
  - Docker
- **Build Tool**: Maven

---

## Data Pipeline

1. **Batch Data**:
   - 100,000 auto-generated demographic records including:
     - `Id`
     - `Age`
     - `Gender`
     - `State`
     - `Country`
2. **Streaming Data**:
   - Real-time purchase events produced every second with:
     - `Id`
     - `campaignID`
     - `orderID`
     - `total_amount`
     - `units`
     - `tags` (click/purchased)
3. **Integration**:
   - Kafka produces events in Avro format.
   - Spark Streaming joins batch and real-time data.
   - MySQL stores demographic data.
   - Kafka Connect pushes events to InfluxDB.
   - Grafana visualizes data from InfluxDB and MySQL.

---

## Approach

- **Event Production**: Kafka generates and consumes user purchase events in Avro format.
- **Stream Processing**: Spark Streaming joins demographic and purchase data.
- **Data Storage**: MySQL for demographic data; InfluxDB for time-series data.
- **Visualization**: Grafana displays interactive and real-time dashboards.
- **Deployment**: Tools are containerized using Docker and orchestrated with `docker-compose`.

---

## High-Level Architecture

1. **Kafka**: Real-time ingestion of user events.
2. **Spark Streaming**: Processes and joins batch and streaming data.
3. **MySQL**: Stores static demographic data.
4. **InfluxDB**: Manages time-series data for real-time visualization.
5. **Grafana**: Displays comprehensive dashboards with insights into user activity.

---

## Key Takeaways

- Build real-time, low-latency Spark-Streaming jobs.
- Learn core concepts of Kafka, Spark Streaming, and time-series databases.
- Integrate InfluxDB with Grafana for dynamic visualizations.
- Deploy tools using Docker and troubleshoot local setups.
- Explore the fine-tuning of frameworks using configuration parameters.

---

## Getting Started

1. Clone the repository.
2. Set up Docker and start the services using `docker-compose`.
3. Configure Kafka topics, Spark Streaming jobs, and database connections.
4. Access the Grafana dashboard to monitor real-time analytics.

---


