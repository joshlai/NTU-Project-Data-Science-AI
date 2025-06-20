
    select
      count(*) as failures,
      count(*) != 0 as should_warn,
      count(*) != 0 as should_error
    from (
      
    
  
    
    



select industry
from `deft-beacon-354008`.`stock_analysis`.`dim_info`
where industry is null



  
  
      
    ) dbt_internal_test