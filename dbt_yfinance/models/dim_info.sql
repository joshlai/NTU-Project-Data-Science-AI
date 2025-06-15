{{ 
    config(
        materialized='table'
    )
}}

SELECT
  ticker_symbol,
  company_description,
  company_name,
  country,
  industry,
  sector
FROM {{source('stock_analysis', 'stock_info')}}