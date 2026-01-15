# Fraud detection data warehouse
A data warehouse project that took simulated credit card transaction data to analyze and detect potential fraudulent activity. Includes synthetic datasets, MySQL schema design, ETL pipeline, and analytical queries for fraud trend evaluation.


Summary of Files

Data

Generates synthetic customer and credit card transaction data for fraud detection testing using Python's Faker library. Creates 5,000 fake customers and 100,000 transactions with vague but realistic attributes and a small percentage labeled as fraudulent with no bias, outputting CSV files for data warehousing and analytics use.


Models

Builds and evaluates simple fraud detection models using the generated customer and transaction data. The script engineers demographic and behavioral features, merges datasets, and trains Logistic Regression, Decision Tree, and KNN to predict fraudulent transactions,and outputs model performance metrics.

SQL

SQL scripts used to review, validate, and analyze data within the fraud detection data warehouse. The queries support data quality checks, exploratory analysis, fraud pattern identification, customer behavior analysis, and summary metrics used for reporting and model development
