import pandas as pd

left = pd.DataFrame({'key':['k0','k1','k2','k3'],'a':['a0','a1','a2','a3'],'b':['b0','b1','b2','b3']})
                                        #   key   a   b
                                        # 0  k0  a0  b0
                                        # 1  k1  a1  b1
                                        # 2  k2  a2  b2
                                        # 3  k3  a3  b3
right = pd.DataFrame({'key':['k0','k1','k2','k3'],'c':['c0','c1','c2','c3'],'d':['d0','d1','d2','d3']})
                                        #   key   c   d
                                        # 0  k0  c0  d0
                                        # 1  k1  c1  d1
                                        # 2  k2  c2  d2
                                        # 3  k3  c3  d3


# res = pd.merge(left,right,on='key')    #类似于SQL中的inner join 合并

                                        #   key   a   b   c   d
                                        # 0  k0  a0  b0  c0  d0
                                        # 1  k1  a1  b1  c1  d1
                                        # 2  k2  a2  b2  c2  d2
                                        # 3  k3  a3  b3  c3  d3
# 如果是考虑两列合并的话用列表  # res = pd.merge(left,right,on=['key','key2'……])  属于inner join
# how = ['left','right','inner','outer'] 与SQL类似
# indicator 可以展示如何合并