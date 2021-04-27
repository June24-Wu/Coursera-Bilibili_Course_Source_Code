
################  矩阵的合并 ######################
#import numpy as np
# a=np.array([1,1,1])
# b=np.array([2,2,2])


# C= np.vstack((a,b))  # vertical stack  上下合并数列       结果 [[1 1 1] [2 2 2]]
# D= np.hstack((a,b)) # horizontal stack  上下合并数列      结果 [1 1 1 2 2 2]

# E= a[np.newaxis, :]   # 在横向新添一个维度      结果 [[1 1 1]]
# F= a[:, np.newaxis]    # 在纵向向新添一个维度      结果是1列3行的1矩阵

# b= b[:,np.newaxis]
# a= a[:,np.newaxis]
# print(np.hstack((a,b)))  # 增加维度后的纵向合并


# c = np.vstack((a,b))
# print(np.concatenate((c,c,c), axis=0)) #矩阵的横向合并
# print(np.concatenate((c,c,c), axis=1)) #矩阵的纵向合并



