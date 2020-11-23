import tushare as ts
import pickle
import  json
import time
import numpy as np
import os
_root=os.path.dirname(__file__)
_data_root=os.path.join(os.path.dirname(_root),'data')
def get_time_stamp(t):
    time_stamp = time.strftime('%Y%m%d',time.localtime(t))
    return time_stamp
def _get_filename(t=None):
    t=t or time.time()
    return 'stock-info-%s.txt'%(get_time_stamp(t))

def _get_default_stock_info_path(t=None):
    t = t or time.time()
    return os.path.join(_data_root,_get_filename(t))
def get_stocks_tushare():
    stock_info = ts.get_stock_basics()
    stocks=df2dict(stock_info)
    return stocks

def df2dict(df):
    keys=list(df.index)
    names=list(df.keys())
    dic={}
    for name in names:
        column=df[name]
        for k in keys:
            v=column[k]
            if isinstance(v,np.int64):
                v=int(v)
            if not k in dic.keys():
                dic[k]={}
            dic[k][name]=v
    for k in keys:
        dic[k]['code']=k

    return dic

def gen_stock_info(path=None):
    path=path or _get_default_stock_info_path()
    stocks = get_stocks_tushare()
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(stocks, f, ensure_ascii=False, indent=2)

# gen_stock_info()
# print(time.time())
def load_china_stock_info(path=None):
    ref_time=1606138638.9840372
    path=path or _get_default_stock_info_path(ref_time)
    with open(path,'r',encoding='utf-8') as f:
        stock_info=json.load(f)
    return stock_info

def get_stock_codes():
    stocks=load_china_stock_info()
    codes=list(stocks.keys())
    return codes
