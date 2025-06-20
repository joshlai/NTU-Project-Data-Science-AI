
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select company_description
from `deft-beacon-354008`.`stock_analysis`.`dim_info`
where company_description is null



  
  
      
    ) dbt_internal_test