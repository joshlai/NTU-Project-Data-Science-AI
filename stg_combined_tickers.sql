with source as (
    select * from {{ source('yfinance_econdata', 'combined_tickers') }}
),
renamed as (
    select
        cast(date as date) as trade_date,
        upper(ticker) as ticker,
        open,
        high,
        low,
        close,
        volume
    from source
)

select * from renamed
