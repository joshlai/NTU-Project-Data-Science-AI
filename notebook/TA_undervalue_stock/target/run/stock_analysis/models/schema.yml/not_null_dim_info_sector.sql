
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select sector
from `deft-beacon-354008`.`stock_analysis`.`dim_info`
where sector is null



  
  
      
    ) dbt_internal_test