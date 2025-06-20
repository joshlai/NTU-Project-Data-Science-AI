

WITH dup_data AS (
SELECT
  t.ticker_symbol,
  DATE(t.date) AS date,
  t.close_price,
  t.high_price,
  t.low_price,
  t.open_price,
  t.stock_splits,
  t.dividend,
  t.volume_traded,
  f.GDP_growth_rate,
  f.UMCSENT,
  f.inflation_rate,
  f.interest_rate,
  f.unemployment_rate,
  f.industrial_production,
  f.ten_yr_treasury,
  i.book_value_per_share,
  i.forward_eps,
  i.forward_pe,
  i.market_cap,
  i.trailing_eps,
  i.trailing_pe,
  ta.ema_50,
  ta.rsi_14,
  ta.sma_50
FROM `deft-beacon-354008`.`stock_analysis`.`combined_tickers` t
LEFT JOIN `deft-beacon-354008`.`stock_analysis`.`fred` f
  ON DATE(t.date) = DATE(f.date)
LEFT JOIN `deft-beacon-354008`.`stock_analysis`.`stock_info` i
  ON t.ticker_symbol = i.ticker_symbol AND DATE(t.date) BETWEEN '2025-04-01' AND '2025-06-30'
LEFT JOIN `deft-beacon-354008`.`stock_analysis`.`techincal_indicator` ta
  ON DATE(t.date) = DATE(ta.date) and t.ticker_symbol = ta.ticker_symbol
)
SELECT 
  ticker_symbol,
  date,
  ANY_VALUE(close_price) AS close_price,
  ANY_VALUE(high_price) AS high_price,
  ANY_VALUE(low_price) AS low_price,
  ANY_VALUE(open_price) AS open_price,
  ANY_VALUE(stock_splits) AS stock_splits,
  ANY_VALUE(dividend) AS dividend,
  ANY_VALUE(volume_traded) AS volume_traded,
  ANY_VALUE(GDP_growth_rate) AS GDP_growth_rate,
  ANY_VALUE(UMCSENT) AS UMCSENT,
  ANY_VALUE(inflation_rate) AS inflation_rate,
  ANY_VALUE(interest_rate) AS interest_rate,
  ANY_VALUE(unemployment_rate) AS unemployment_rate,
  ANY_VALUE(ten_yr_treasury) AS ten_yr_treasury,
  ANY_VALUE(industrial_production) AS industrial_production,
  ANY_VALUE(forward_eps) AS forward_eps,
  ANY_VALUE(forward_pe) AS forward_pe,
  ANY_VALUE(market_cap) AS market_cap,
  ANY_VALUE(trailing_eps) AS trailing_eps,
  ANY_VALUE(trailing_pe) AS trailing_pe,
  ANY_VALUE(ema_50) AS ema_50,
  ANY_VALUE(rsi_14) AS rsi_14,
  ANY_VALUE(sma_50) AS sma_50,
  ANY_VALUE(book_value_per_share) AS book_value_per_share
FROM dup_data 
GROUP BY ticker_symbol, date