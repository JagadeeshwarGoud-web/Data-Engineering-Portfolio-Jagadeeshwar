-- orders_schema.sql
-- Database schema design for the E-commerce ETL project

CREATE TABLE raw.orders (
    order_id INT PRIMARY KEY,
    amount DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE analytics.orders_summary (
    order_id INT,
    amount DECIMAL(10,2),
    processed_date DATE,
    order_category VARCHAR(50)
);
