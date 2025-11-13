-- dbt model: orders_transform.sql
-- Transforming raw order data into clean analytics table

WITH raw_orders AS (
    SELECT 
        order_id,
        amount,
        CURRENT_DATE AS processed_date
    FROM {{ source('raw', 'orders') }}
)

SELECT 
    order_id,
    amount,
    processed_date,
    CASE 
        WHEN amount >= 150 THEN 'High Value'
        ELSE 'Regular'
    END AS order_category
FROM raw_orders;
