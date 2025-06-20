
    
    

with child as (
    select ticker_symbol as from_field
    from `deft-beacon-354008`.`stock_analysis`.`fact_security`
    where ticker_symbol is not null
),

parent as (
    select ticker_symbol as to_field
    from `deft-beacon-354008`.`stock_analysis`.`dim_info`
)

select
    from_field

from child
left join parent
    on child.from_field = parent.to_field

where parent.to_field is null


