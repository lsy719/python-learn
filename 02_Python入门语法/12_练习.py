name = "Lsy"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.0023
growth_dats = 365
res = stock_price * stock_price_daily_growth_factor ** growth_dats
print(f"公司：{name}, 股票代码：{stock_code}, 当前股价:{stock_price}")
print("每日增长系数是：%f, 经过%d天的增长后，股价到了：%.2f" % (stock_price_daily_growth_factor, growth_dats, res))

