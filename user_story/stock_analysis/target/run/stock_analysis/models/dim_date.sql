
  
    

    create or replace table `dsai-project-462603`.`stock_analysis`.`dim_date`
      
    
    

    OPTIONS()
    as (
      

WITH deduplicated_dates AS (
    SELECT DISTINCT date
    FROM `dsai-project-462603`.`stock_analysis`.`combined_tickers`
)
SELECT
    DATE(date) AS date,
    EXTRACT(YEAR FROM date) AS year,
    EXTRACT(MONTH FROM date) AS month,
    EXTRACT(DAY FROM date) AS day,
    EXTRACT(QUARTER FROM date) AS quarter,
    FORMAT_TIMESTAMP('%A', date) AS day_of_week
FROM 
    deduplicated_dates
    );
  