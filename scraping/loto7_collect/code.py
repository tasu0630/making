#random.choiceによる指定確率

import pandas as pd
import numpy as np
from decimal import Decimal

#効率の良い書き方を考える必要あり
element_list = ["1","2","3","4","5","6","7","8","9","10",
                "11","12","13","14","15","16","17","18","19","20",
                "21","22","23","24","25","26","27","28","29","30",
                "31","32","33","34","35","36","37"]

#percentを1にするために、割合の低い物の出る確率を上げる
#Decimalでfloatの丸め誤差をなくす
# 12(0.021→0.022)
prob_list = [Decimal("0.026"),Decimal("0.023"),Decimal("0.026"),Decimal("0.03"),Decimal("0.023"),Decimal("0.029"),Decimal("0.027"),Decimal("0.027"),Decimal("0.032"),Decimal("0.029"),
             Decimal("0.028"),Decimal("0.022"),Decimal("0.03"),Decimal("0.027"),Decimal("0.034"),Decimal("0.022"),Decimal("0.028"),Decimal("0.025"),Decimal("0.023"),Decimal("0.025"),
             Decimal("0.029"),Decimal("0.026"),Decimal("0.03"),Decimal("0.028"),Decimal("0.022"),Decimal("0.028"),Decimal("0.029"),Decimal("0.029"),Decimal("0.025"),Decimal("0.03"),
             Decimal("0.028"),Decimal("0.027"),Decimal("0.024"),Decimal("0.029"),Decimal("0.03"),Decimal("0.029"),Decimal("0.021")]

#元の確率(1.0290000000000006)
#a=(0.026+0.023+0.026+0.03+0.023+0.029+0.027+0.027+0.032+0.029+
     #0.028+0.021+0.03+0.027+0.034+0.022+0.028+0.025+0.023+0.025+
     #0.029+0.026+0.03+0.028+0.022+0.028+0.029+0.029+0.025+0.03+
     #0.03+0.028+0.027+0.024+0.029+0.03+0.029+0.021)
#print(a)

#７列を表示
sample_size = 7

#list作成
t_list=[]
tmp=[]
new=[]

#4500(300*5*3枚)
#数字の被りがあった場合の改善が必要　※被った場合、確率の高い15、に入れ替える
for i in range(15):
    tmp=(np.random.choice(a=element_list, size=sample_size, p=prob_list))
    
    for j in range(7):
        for k in range(7):
            #同じ要素を比べた時
            if j==k:
                break
            #数字の被りがあった場合
            elif tmp[j]==tmp[k]:
                new=(np.random.choice(a=element_list, size=sample_size, p=prob_list))
                tmp[j]=new[0]
                
    t_list.append(tmp)

df=pd.DataFrame(t_list)
df.to_csv("code.csv")
