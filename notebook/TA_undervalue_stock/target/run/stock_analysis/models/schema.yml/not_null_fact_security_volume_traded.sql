
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select volume_traded
from `deft-beacon-354008`.`stock_analysis`.`fact_security`
where volume_traded is null



  
  
      
    ) dbt_internal_test