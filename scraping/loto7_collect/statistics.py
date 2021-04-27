#要素の総数を比べる
#グラフ化

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#CSVの読み込み
df=pd.read_csv("/Users/tasuke0630/making/scraping/loto7_collect/quantity.csv",index_col=0)

detail=df.plot.bar(title="Comparison",x="number",y="num")


plt.show()
