
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select date
from `dsai-project-462603`.`stock_analysis`.`fact_security`
where date is null



  
  
      
    ) dbt_internal_test