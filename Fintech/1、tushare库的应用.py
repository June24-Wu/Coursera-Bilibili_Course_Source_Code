import pandas as pd
import tushare as ts
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdate
import mpl_finance as mpf # 画K线图
# ----------------------------------
style.use('ggplot')  # 设置画图格式
pd.set_option('display.max_columns', None)
pd.set_option('display.max_row', None)  # 设置最长的长 和 列


# -------------------------------------
def get_data():
    data = ts.get_hist_data('000001')  # 得到数据

    # 保存文件 csv
    data.to_csv('000001.csv')


def read_data():
    df_read_csv = pd.read_csv('000001.csv', parse_dates=True, index_col=0)  # 进行数据的解析
    data_new = moving_average_7days(df_read_csv)  # 计算7天移动平均线
    # print(data_new.tail(10))



    # show_data_normal_picture(data_new)  # 展现普通的图

    show_K_xian_tu(data_new)   # 画K线图


def moving_average_7days(data):  # 移动平均
    data_reverse = data.sort_index(ascending=True)

    data_reverse['ma7'] = data_reverse['close'].rolling(window=7).mean()  # 以收盘价进行加权平均

    return data_reverse


def show_data_normal_picture(data_list=None):  # 展现普通的图
    ax1 = plt.subplot2grid((9, 10), (0, 0), rowspan=7, colspan=10)
    ax2 = plt.subplot2grid((9, 10), (7, 0), rowspan=2, colspan=10, sharex=ax1)
    ax1.plot(data_list.index, data_list['close'])
    ax1.plot(data_list.index, data_list['ma7'])
    ax2.bar(data_list.index, data_list['volume'])
    plt.show()
    return None



def show_K_xian_tu(data_list):
    ax1 = plt.subplot2grid((9, 10), (0, 0), rowspan=7, colspan=10)
    ax2 = plt.subplot2grid((9, 10), (7, 0), rowspan=2, colspan=10, sharex=ax1)
    data_time = data_list.index
    print(data_time)
    data_list = data_list.reset_index()

    data_list['date'] = data_list['date'].map(mdate.date2num)  # 把日期形式改变成数字形式方便matplotlib读取

    mpf.candlestick2_ochl(ax=ax1, opens=data_list['open'], closes=data_list['close'], highs=data_list['high'], lows=data_list['low'], width=1,colorup='red',colordown='green')
    ax2.bar(data_list.index, data_list['volume'])
    plt.xticks(data_list.index[::200],data_time[::200])
    plt.show()





if __name__ == "__main__":
    read_data()
