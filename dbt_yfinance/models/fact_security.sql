{{ 
    config(
        materialized='table'
    )
}}

SELECT
  row_number() OVER (ORDER BY t.ticker_symbol) AS fact_security_id,
  t.ticker_symbol,
  DATE(t.date) AS date,
  t.close_price,
  t.dividend,
  t.high_price,
  t.low_price,
  t.open_price,
  t.stock_splits,
  t.volume_traded,
  f.GDP_growth_rate,
  f.UMCSENT,
  f.inflation_rate,
  f.interest_rate,
  f.unemployment_rate,
  i.dividendYield,
  i.forward_eps,
  i.forward_pe,
  i.market_cap,
  i.trailing_eps,
  i.trailing_pe,
  ta.ema_50,
  ta.rsi_14,
  ta.sma_50
FROM {{source('stock_analysis', 'combined_tickers')}} t
LEFT JOIN {{source('stock_analysis', 'fred')}} f
  ON DATE(t.date) = DATE(f.date)
LEFT JOIN {{source('stock_analysis', 'stock_info')}} i
  ON t.ticker_symbol = i.ticker_symbol AND DATE(t.date) BETWEEN '2025-04-01' AND '2025-06-30'
LEFT JOIN {{source('stock_analysis','techincal_indicator')}} ta
  ON DATE(t.date) = DATE(ta.date) and t.ticker_symbol = ta.ticker_symbol
