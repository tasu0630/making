#個数と割合の表示

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt


#CSVの読み込み
df=pd.read_csv("/Users/tasuke0630/making/scraping/loto7_collect/loto7_detail.csv",index_col=0)

for i in range(37):
    df_bool=(df==i+1)
    num=(df_bool.sum())
    n=num[0]/2800

    #round() 小数を任意の桁数でまとめる
    a=round(n,3)
    print("値",i+1,":",num[0],"個",a,"per")
