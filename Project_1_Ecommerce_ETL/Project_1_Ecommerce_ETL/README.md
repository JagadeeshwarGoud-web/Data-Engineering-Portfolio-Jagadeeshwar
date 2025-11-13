# Project 1 — E-commerce ETL & Data Warehouse

## Overview  
This project demonstrates an end-to-end **data engineering pipeline** for an e-commerce company.  
It extracts transactional data from APIs, loads it into Amazon S3, transforms it using dbt,  
and finally stores analytics-ready data in **Amazon Redshift**.

---

## Architecture  
1. **Extract** → Python scripts scheduled with **Apache Airflow** pull raw data from APIs.  
2. **Transform** → **dbt** models clean and shape data into a star schema.  
3. **Load** → Transformed data is loaded into **Amazon Redshift**.  
4. **Monitor** → Airflow DAG monitors tasks and alerts on failures.

---

## Folder Structure  

---

## Technologies Used  
Python | Apache Airflow | dbt | AWS S3 | Redshift | SQL | Boto3 | Parquet | Slack Alerts  

---

## How to Run  
1. Clone this repository to your system.  
2. Install dependencies:  
   ```bash
   pip install apache-airflow dbt-core boto3
   airflow webserver -p 8080
ecommerce_etl_dag


airflow webserver -p 8080
