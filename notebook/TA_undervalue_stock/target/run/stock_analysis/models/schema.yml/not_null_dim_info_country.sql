
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select country
from `deft-beacon-354008`.`stock_analysis`.`dim_info`
where country is null



  
  
      
    ) dbt_internal_test