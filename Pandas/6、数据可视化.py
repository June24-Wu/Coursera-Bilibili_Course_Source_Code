# -----------------------------------plot data---------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -----------------1.Series  系列--------------
# data = pd.Series(np.random.randn(10000),index=np.arange(10000))
# data = data.cumsum()
# print(data)
# data.plot()
# plt.show()
# -----------------1.dataframe  系列--------------
data=pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('abcd'))
print(data)
data.plot()
plt.show()





