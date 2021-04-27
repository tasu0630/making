#pythonで準備されてるライブラリー
import os
from time import sleep

#別途でインストールするライブラリー
import pandas as pd
import requests

IMAGE_DIR="./images/"

#CSVの読み込み
df=pd.read_csv("/Users/tasuke0630/making/scraping/image_collect/champions_league_v.csv")

#directoryの確認
if os.path.isdir(IMAGE_DIR):
    print("既にあります")
else:
    #特定の場所にディレクトリを作る
    os.chdir("/Users/tasuke0630/making/scraping/image_collect")
    os.makedirs(IMAGE_DIR)

#画像の保存(先頭から5個)
for name,img_url in zip(df.name[:10],df.img_url[:10]):
    image=requests.get(img_url)
    with open(IMAGE_DIR+name+'.jpg','wb') as f:
        f.write(image.content)

    sleep(1)
