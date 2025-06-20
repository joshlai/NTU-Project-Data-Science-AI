
    
    

with dbt_test__target as (

  select company_name as unique_field
  from `dsai-project-462603`.`stock_analysis`.`dim_info`
  where company_name is not null

)

select
    unique_field,
    count(*) as n_records

from dbt_test__target
group by unique_field
having count(*) > 1


