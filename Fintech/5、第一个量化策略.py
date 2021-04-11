"""
1、股票池为沪深300股票的所有成分股
2、如果当前股价小于10元且不持仓，则买入
3、如果当前股价比买入时上涨25%，则清仓止盈
4、如果当前股票比买入时下跌10%，则清仓止损
"""
import pandas as pd
import numpy as np
import tushare as ts
import pickle


# 得到所有的开盘价
def get_hs300_data(start_date):
    with open(r'D:\PyCharmproject\金融科技\hu_shen_300.pickle', 'rb') as f:
        tickers_mod = pickle.load(f)

    ts.set_token('48791ea5c685296f9cbdef198850b0a47f23a3d5a298263af39718f2')
    pro = ts.pro_api()
    stock_price_df = pd.DataFrame()
    for number , ticker in enumerate(tickers_mod):
        df = pro.daily(ts_code = ticker,start_date = start_date)
        df.set_index('trade_date',inplace=True)    # 设置index
        df.rename(columns={'open':ticker},inplace=True)  # 设置收盘价的特征标签为股票代码
        df.drop(['ts_code','close','high','low','pre_close','change','pct_chg','vol','amount'],axis=1,inplace=True)
        if stock_price_df.empty:
            stock_price_df = df
        else:
            stock_price_df = stock_price_df.join(df,how='outer')
            print(number)
    stock_price_df.sort_index(ascending=True,inplace=True)
    stock_price_df.dropna(axis=0,how='any',inplace=True)
    stock_price_df.to_csv('./5、第一个量化策略（开盘价合集）.csv')


def analyze():
    df = pd.read_csv('./5、第一个量化策略（开盘价合集）.csv').set_index('trade_date')
    print(df)
    with open(r'D:\PyCharmproject\金融科技\hu_shen_300.pickle', 'rb') as f:
        tickers_mod = pickle.load(f)
    buy_ticker = {}
    hold = []
    money = 100000
    buy_ticker['1'] = 10
    for row in df.iterrows():
        try:
            data = row[1]
            to_buy = list(data[data.values <10].index)
            for i in to_buy:
                if not hold.__contains__(i):
                    hold.append(i)
                    buy_ticker[i] = data[i]
                    money -= data[i] * 100
            for t in hold:
                if data[t] >= 1.25 *  buy_ticker[t]:
                    money += data[t] *100
                    hold.remove(t)
                    del buy_ticker[t]
                if data[t] <= 0.9 *  buy_ticker[t]:
                    money += data[t] *100
                    hold.remove(t)
                    del buy_ticker[t]
        except:
            continue
    for i in hold:
        money += df.iloc[-1][i] * 100
        hold.remove(i)
    print(money)
    print(hold)









if __name__ == "__main__":
    # -------------读取数据---------------
    # start_date = '20200101'
    # get_hs300_data(start_date)


    # -------------执行数据-------------------
    analyze()


