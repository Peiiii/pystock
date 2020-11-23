import pandas_datareader as pdr


def get_stock_info_form_yahoo(*args,**kwargs):
    '''
    Example:
    >>> get_stock_info_form_yahoo('003019.sz','2010-01-01','2020-12-31')
    :param args:
    :param kwargs:
    :return:
    '''
    return pdr.get_data_yahoo(*args,**kwargs)