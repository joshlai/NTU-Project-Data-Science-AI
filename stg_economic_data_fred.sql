with source as (
    select * from {{ source('yfinance_econdata', 'economic_data_fred') }}
),

unpivoted as (
    select
        cast(date as date) as event_date,
        indicator,
        value
    from source
    unpivot(value for indicator in (CPI, Federal_Funds_Rate, Unemployment_Rate, GDP))
)

select
    event_date,
    indicator,
    value as data_value
from unpivoted
