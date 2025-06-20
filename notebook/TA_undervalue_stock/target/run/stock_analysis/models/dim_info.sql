
  
    

    create or replace table `deft-beacon-354008`.`stock_analysis`.`dim_info`
      
    
    

    OPTIONS()
    as (
      

SELECT
  ticker_symbol,
  company_description,
  company_name,
  country,
  industry,
  sector
FROM `deft-beacon-354008`.`stock_analysis`.`stock_info`
    );
  