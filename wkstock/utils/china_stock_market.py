import re

china_market_names = [
    '上证综指',
    '深圳成指',
    '中小板',
    '创业板',
    '科创板',
]

def get_bankuai(code):
    assert isinstance(code,str)
    if code[:3] == '002':
        return 2
    elif code[:2]=='00':
        return 1
    elif code[:3]=='300':
        return 3
    elif code[:2]=='60':
        return 0
    elif code.startswith('688'):
        return 4
    else:
        raise Exception('unknown code %s.'%(code))
def get_bankuai_name(code):
    return china_market_names[get_bankuai(code)]

def get_yahoo_code(code):
    bankuai=get_bankuai(code)
    if bankuai==0 or bankuai==4:
        return code+'.ss'
    elif bankuai==1 or bankuai==2 or bankuai==3:
        return code+'.sz'
    else:
        raise Exception('unknown code %s .'%(code))