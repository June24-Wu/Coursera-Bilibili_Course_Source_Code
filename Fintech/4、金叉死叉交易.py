import numpy as np
import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
from matplotlib import style
style.use('seaborn')

def moving_average_5days(data):  # 移动平均
    data_reverse = data.sort_index(ascending=True)

    data_reverse['ma5'] = data_reverse['close'].rolling(window=5).mean()  # 以收盘价进行加权平均

    return data_reverse

def moving_average_30days(data):  # 移动平均
    data_reverse = data.sort_index(ascending=True)

    data_reverse['ma30'] = data_reverse['close'].rolling(window=30).mean()  # 以收盘价进行加权平均

    return data_reverse

def gold_and_death_cross_date(data):   # 得到金叉和死叉的日期
    gold_cross_date_list = []
    death_cross_date_list = []
    for i in range(1,len(data)):
        if data['ma5'][i:i+1].values > data['ma30'][i:i+1].values and data['ma5'][i-1:i].values < data['ma30'][i-1:i].values:
            gold_cross_date_list.append(data.index[i])
        if data['ma5'][i:i+1].values < data['ma30'][i:i+1].values and data['ma5'][i-1:i].values > data['ma30'][i-1:i].values:
            death_cross_date_list.append(data.index[i])
    return gold_cross_date_list , death_cross_date_list


def trade(gold_cross_date_list,death_cross_date_list,money = 100000):
    hold = 0   # 持有的股票
    sr1 = pd.Series(1,index=gold_cross_date_list)
    sr2 = pd.Series(0,index=death_cross_date_list)
    sr = pd.concat([sr1,sr2],axis=0).sort_index(ascending=True)
    # print(sr)
    for i in range(len(sr)):
        p = data['open'][sr.index[i]]
        if sr.iloc[i] == 1: # 金叉
            buy = money // (100*p)
            hold += buy*100
            money -= buy*100 * p
        else:
            money += hold*p
            hold = 0

    p = data['open'].iloc[-1]
    final_money = p*hold + money
    print('金叉日期数量为：',len(sr1))
    print('死叉日期数量为：', len(sr2))
    return final_money








if __name__ == "__main__":
    ts.set_token('48791ea5c685296f9cbdef198850b0a47f23a3d5a298263af39718f2')
    pro = ts.pro_api()

    ts_code = input('请输入所需要的股票代码（例如600519.SH）:')
    start_date = input('请输入股票查询开始的日期（例如20190101）：')
    money = int(input('请输入你的初始资金：'))





    data = pro.daily(ts_code = ts_code,start_date = start_date)
    print(data)
    data.set_index('trade_date',inplace=True)
    data = moving_average_5days(data)
    data = moving_average_30days(data)
    data.dropna(how='any',axis=0,inplace=True)

    gold_cross_date_list , death_cross_date_list = gold_and_death_cross_date(data)
    finally_money = trade(gold_cross_date_list,death_cross_date_list,money)
    print('初始的资金为:', money)
    print('最终的资金为:',finally_money)

