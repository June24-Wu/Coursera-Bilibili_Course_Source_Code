import pandas as pd
import numpy as np
date = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),index=date,columns=['A','B','C','D'])

df.iloc[1,2] = np.nan
df.iloc[0,1] = np.nan

                            #              A     B     C   D
                            # 2013-01-01   0   NaN   2.0   3
                            # 2013-01-02   4   5.0   NaN   7
                            # 2013-01-03   8   9.0  10.0  11
                            # 2013-01-04  12  13.0  14.0  15
                            # 2013-01-05  16  17.0  18.0  19
                            # 2013-01-06  20  21.0  22.0  23
                                    #存在NAN数据
# ----------------------------------------------------------------------------------------------
# print(df.dropna())     # 默认为  axis=0，how = any
# how = 'any' or 'all'  其中any是其中一行有nan就丢掉这一整行， all是当所有数据都为nan时候才丢掉
                            #              A     B     C   D
                            # 2013-01-03   8   9.0  10.0  11
                            # 2013-01-04  12  13.0  14.0  15
                            # 2013-01-05  16  17.0  18.0  19
                            # 2013-01-06  20  21.0  22.0  23




# print(df.dropna(axis=1))
                            #              A   D
                            # 2013-01-01   0   3
                            # 2013-01-02   4   7
                            # 2013-01-03   8  11
                            # 2013-01-04  12  15
                            # 2013-01-05  16  19
                            # 2013-01-06  20  23

# ------------------------------填充nan数据---------------------------------------------
# print(df.fillna(value=0))  # 将nan数据填充为0
                            #              A     B     C   D
                            # 2013-01-01   0   0.0   2.0   3
                            # 2013-01-02   4   5.0   0.0   7
                            # 2013-01-03   8   9.0  10.0  11
                            # 2013-01-04  12  13.0  14.0  15
                            # 2013-01-05  16  17.0  18.0  19
                            # 2013-01-06  20  21.0  22.0  23
# -------------------------------检查nan数据的存在--------------------------------------------
# print(df.isnull())  # isnull是用来检查整个矩阵的
                            #                 A      B      C      D
                            # 2013-01-01  False   True  False  False
                            # 2013-01-02  False  False   True  False
                            # 2013-01-03  False  False  False  False
                            # 2013-01-04  False  False  False  False
                            # 2013-01-05  False  False  False  False
                            # 2013-01-06  False  False  False  False
# print(np.any(df.isnull()) == True)  # 只要存在一个nan就会返回True
                            # True

