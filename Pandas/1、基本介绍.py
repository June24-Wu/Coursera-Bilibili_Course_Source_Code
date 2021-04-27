import pandas as pd
import numpy as np


# s = pd.Series([1,3,6,np.nan,44,1])
# print(s)


#                                     创建一个数据库 ###
s = pd.date_range('20190101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=s,columns=['a','b','c','d'])
# print(df)
# 没有定义 index 和 column 时，索引默认为0,1,2,3

# df.index 返回的是所有行的索引值
# df.columns 返回的是所有列的索引值
# df.values 返回的所有的值
# print(df.describe()) # 打印所有列数值的方差、平均值、分位数等等
# sort_index   ,sort valuse 都是排列数据
