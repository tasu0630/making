#要素の総数
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#CSVの読み込み
df=pd.read_csv("/Users/tasuke0630/making/scraping/loto7_collect/loto7_detail.csv",index_col=0)


t_list=[]
num=[]

for i in range(37):
    #TrueとFalseの判別
    df_bool=(df==i+1)
    #Trueの数の総数
    num=(df_bool.sum())

    tmp={
        "number":i+1,
        "num":num[0]
    }

    t_list.append(tmp)

df=pd.DataFrame(t_list)
df.to_csv("quantity.csv")
