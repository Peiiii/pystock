import wkstock
import pandas_datareader as pdr
import random
stocks=wkstock.load_china_stock_info()
# print(stocks)
codes=wkstock.get_stock_codes()
print(codes)

# x=pdr.get_data_yahoo('000816.sz')
# x=pdr.get_data_yahoo('688179.ss')
x=wkstock.get_yahoo_code(random.choice(codes))

print(x)
x=wkstock.get_stock_info_form_yahoo(x,'2010-01-01','2020-12-31')
print(x)