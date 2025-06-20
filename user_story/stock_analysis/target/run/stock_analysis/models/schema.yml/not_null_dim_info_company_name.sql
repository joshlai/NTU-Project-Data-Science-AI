
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select company_name
from `dsai-project-462603`.`stock_analysis`.`dim_info`
where company_name is null



  
  
      
    ) dbt_internal_test