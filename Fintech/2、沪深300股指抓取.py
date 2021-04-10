import tushare as ts
from matplotlib import style
import pandas as pd
import pickle
import os
import html_crawler
# ------------------------------------------
style.use('ggplot')  # 设置画图格式
pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)  # 设置最长的长 和 列










# --------------------------------爬虫代码-------------------------------------------


def find_csi_300():  #  在维基百科上找到沪深300的股票代码
    url = r'https://en.wikipedia.org/wiki/CSI_300_Index'
    soup = html_crawler.get_and_parse_html(url)
    soup = soup.find_all('table',class_ =r"wikitable sortable")
    soup = soup[1]
    soup = soup.find('tbody')
    list = []
    for i in soup.find_all('tr'):
        i = i.find_all('td')
        try:
            i = i[0].string
        except:
            continue
        list.append(str(i).strip())
    print(list)
    return list
# -------------------------------------------------------------------------------------------------------













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










def get_data_from_tushare(reload_CSI_300 = False):
    # ------------------------------访问-------------------------------------
    ts.set_token('78f0366a9fb5ef19260bb882a1b7ba8012da8d8288333197684e5b1d')
    pro = ts.pro_api()
    # -------------------------------
    if reload_CSI_300:
        tickers_mod = find_csi_300_2()
    else:
        with open('CSI_tickers.pickle','rb') as f:
            tickers_mod = pickle.load(f)
    if not os.path.exists('沪深300data'):
        os.makedirs('沪深300data')
    for ticker_mod in tickers_mod:
        df = pro.daily(ts_code = ticker_mod)
        df.to_csv('./沪深300data/'+ ticker_mod + '.csv')
        print(ticker_mod)







# -----------------------将数据汇总到一个大表里-------------------------------------------
def put_all_stock_price_into_one_df():
    # 加载股票代码
    with open('CSI_tickers.pickle', 'rb') as f:
        tickers_mod = pickle.load(f)

    all_stock_price_df = pd.DataFrame()
    # print(all_stock_price_df)
    for count , tickers in enumerate(tickers_mod):  # enumerate增加计数器
        df  = pd.read_csv('./沪深300data/'+tickers+'.csv')
        df.set_index('trade_date',inplace=True) # 设置index
        df.rename(columns={'close':tickers},inplace=True)  # 设置收盘价的特征标签为股票代码
        df.drop(['Unnamed: 0','ts_code','open','high','low','pre_close','change','pct_chg','vol','amount'],axis=1,inplace=True)
        if all_stock_price_df.empty:
            all_stock_price_df = df
        else:
            all_stock_price_df = all_stock_price_df.join(df,how='outer')
        print(count)
    all_stock_price_df.sort_index(ascending=False,inplace=True)
    all_stock_price_df.to_csv('./沪深300data/收盘价合集.csv')
    print('储存完成')












if __name__ == "__main__":
    put_all_stock_price_into_one_df()



