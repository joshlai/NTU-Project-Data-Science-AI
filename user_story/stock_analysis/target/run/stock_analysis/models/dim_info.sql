
  
    

    create or replace table `dsai-project-462603`.`stock_analysis`.`dim_info`
      
    
    

    OPTIONS()
    as (
      

SELECT
  ticker_symbol,
  company_description,
  company_name,
  country,
  industry,
  sector
FROM `dsai-project-462603`.`stock_analysis`.`stock_info`
    );
  