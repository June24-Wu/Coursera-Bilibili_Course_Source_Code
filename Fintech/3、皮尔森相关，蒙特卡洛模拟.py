import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import pickle
import numpy as np
import matplotlib
from matplotlib.font_manager import FontProperties
import tushare as ts

# ------------------------------------------------------
style.use("ggplot")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)  # 设置最长的长 和 列
# ------------------------------------------------------


def find_csi_300_2(): # 通过ts.get_hs300s()方法来找到沪深300的code
    CSI_300_df = ts.get_hs300s()
    tickers = CSI_300_df['code'].values  # 转化为列表 002044 000961
    new_tickers = []
    for i in tickers:
        if i[0] == '0' or i[0] == '3':
            i = i + '.SZ'
        if i[0] == '6':
            i = i + '.SH'
        new_tickers.append(i)   # 601238.SH  002044.SZ
    with open('CSI_tickers.pickle','wb') as f:
        pickle.dump(new_tickers,f)
    print(new_tickers)
    return new_tickers








# 计算 保存 和画图
# -------------------------------------皮尔森相关---------------------------------------

def calculate_save_and_plot_pearson_correlation_heatmap():
    df = pd.read_csv('./沪深300data/收盘价合集.csv')
    df_corr = df.pct_change().corr()  # 要先计算百分比的变化，然后再进行皮尔森积
    df_corr.to_csv('./沪深300data/收盘价合集的皮尔森积.csv')
    data = df_corr.values
    print(data.shape)
    #  --------------------------画图---------------------------
    # fig = plt.figure(figsize=(20,8),dpi=80)
    # ax = fig.add_subplot(111)
    #
    # heat_map = ax.pcolor(data,cmap= plt.cm.RdYlGn)
    # fig.colorbar(heat_map)
    # plt.show()
    # --------------------------------------------------


# ------------------------------------------------------------------------------------------------













def Analyze_some_stock():  # 选择两个股票进行分析

    tickers = find_csi_300_2()[:]

    # -------------------保存所选股票的收盘价----------------------
    some_stock_price_df = pd.DataFrame()
    for count , ticker in enumerate(tickers):  # enumerate增加计数器
        df  = pd.read_csv('./沪深300data/'+ ticker +'.csv')
        df.set_index('trade_date',inplace=True)    # 设置index
        df.rename(columns={'close':ticker},inplace=True)  # 设置收盘价的特征标签为股票代码
        df.drop(['Unnamed: 0','ts_code','open','high','low','pre_close','change','pct_chg','vol','amount'],axis=1,inplace=True)
        if some_stock_price_df.empty:
            some_stock_price_df = df
        else:
            some_stock_price_df = some_stock_price_df.join(df,how='outer')
        print(count)
    some_stock_price_df.sort_index(ascending=False,inplace=True)
    some_stock_price_df.to_csv('./沪深300data/精选股票收盘价合集.csv')
    print('储存完成')
    some_stock_price_df = some_stock_price_df.sort_index(ascending=True)
    some_stock_price_df.dropna(axis=0,how='any',inplace=True)





    # ----------------------------回报层面 ------------------------------
    returns_daily = some_stock_price_df.pct_change()  # 计算每天的回报变化


    # 计算每年的平均收益
    returns_annual = returns_daily.mean() * 250  # 000001.SZ    0.070037     000002.SZ    0.153759



    # -------------------------风险层面----------------------------------
    cov_daily = returns_daily.cov()
    cov_annual = cov_daily * 250



    # -------------------------蒙特卡洛模拟--------------------------------
    number_of_portfolio = 10000
    portfolio_return = []
    portfolio_volatility = []
    stock_weight = []

    number_of_asset = len(tickers)   # 分析股票的长度



    for single_portfolio in range(number_of_portfolio):
        weight = np.random.random(number_of_asset)
        weight /= np.sum(weight)   # 使得权重之和等于1
        stock_weight.append(weight)

        returns = np.dot(weight,returns_annual)   # 计算回报率：returns = w1r1 + w2r2
        portfolio_return.append(returns)

        volatility = np.dot(weight,cov_annual)
        volatility = np.dot(weight,volatility.T)
        portfolio_volatility.append(volatility)
    print('计算完成')
    print(stock_weight[2][1])

    # ----------------------------储存数据-------------------------------------
    portfolio = {'回报率':portfolio_return,'风险':portfolio_volatility,}

    for counter , i in enumerate(tickers):
        portfolio[i+'权重'] = [single_weight[counter] for single_weight in stock_weight] # 计算每个股票的权重
    portfolio_df = pd.DataFrame(portfolio)
    portfolio_df.to_csv('./沪深300data/精选股票投资组合.csv')


    # ----------------------------------画图-----------------------------------------------
    style.use('seaborn')
    font = FontProperties(fname=r"C:\Windows\Fonts\simhei.ttf")
    portfolio_df.plot.scatter(x = '风险',y='回报率',grid = True,figsize = (20,8),)
    plt.xlabel('风险',fontproperties=font)
    plt.ylabel('回报率',fontproperties=font)
    plt.show()
















if __name__ == "__main__":
    Analyze_some_stock()



