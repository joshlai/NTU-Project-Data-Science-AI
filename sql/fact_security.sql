SELECT
  t.`ticker_symbol`,
  DATE(t.`date`) as date,
  t.`close_price`,
  t.`dividend`,
  t.`high_price`,
  t.`low_price`,
  t.`open_price`,
  t.`stock_splits`,
  t.`volume_traded`,
  f.`GDP_growth_rate`,
  f.`UMCSENT`,
  f.`inflation_rate`,
  f.`interest_rate`,
  f.`unemployment_rate`,
  i.`dividendYield`,
  i.`company_description`,
  i.`company_name`,
  i.`country`,
  i.`forward_eps`,
  i.`forward_pe`,
  i.`industry`,
  i.`market_cap`,
  i.`sector`,
  i.`trailing_eps`,
  i.`trailing_pe`,
  ta.`date`,
  ta.`ema_50`,
  ta.`rsi_14`,
  ta.`sma_50`,
FROM
  `ntuproj-462609.stock_analysis.combined_tickers` t
LEFT JOIN
  `ntuproj-462609.stock_analysis.fred` f
  ON DATE(t.`date`) = DATE(f.`date`)
LEFT JOIN
  `ntuproj-462609.stock_analysis.stock_info` i
  ON t.ticker_symbol = i.ticker_symbol and DATE(t.`date`) BETWEEN '2025-04-01' AND '2025-06-30'
LEFT JOIN
  `ntuproj-462609.stock_analysis.techincal_indicator` ta
  ON DATE(t.`date`) = DATE(ta.`date`) and t.ticker_symbol = ta.ticker_symbol
;


  

