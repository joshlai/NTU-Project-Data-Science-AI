{{
    config(
        materialized='table'
    )
}}

SELECT
  row_number() over (order by Ticker) as fact_security_id,
  Date as date,
  Ticker as ticker_symbol,
  Close as close_price,
  Open as open_price,
  High as high_price,
  Low as low_price,
  Volume as volume_traded
FROM {{ref('combined_tickers')}}
