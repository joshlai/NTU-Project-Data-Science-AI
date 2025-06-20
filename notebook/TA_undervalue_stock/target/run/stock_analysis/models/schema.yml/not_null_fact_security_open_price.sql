
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select open_price
from `deft-beacon-354008`.`stock_analysis`.`fact_security`
where open_price is null



  
  
      
    ) dbt_internal_test