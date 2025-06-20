
    
    

with child as (
    select date as from_field
    from `deft-beacon-354008`.`stock_analysis`.`fact_security`
    where date is not null
),

parent as (
    select date as to_field
    from `deft-beacon-354008`.`stock_analysis`.`dim_date`
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


