
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select ticker_symbol
from `dsai-project-462603`.`stock_analysis`.`fact_security`
where ticker_symbol is null



  
  
      
    ) dbt_internal_test