# coding=utf-8
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
num = int(input('请输入有多少本书籍'))
a = np.random.random(num)*10  # 书籍评分
year = np.random.randint(2000,2020,num) # 书籍年限
df = pd.DataFrame({'书籍年限' :  year , '书籍评分' : a})
df = df.groupby(by='书籍年限').mean()['书籍评分']

x = df.index
y = df.values
plt.plot(x,y)
plt.xticks(x[::2],x[::2])
plt.show()

