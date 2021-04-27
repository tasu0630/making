from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_path='/Users/tasuke0630/making/scraping/chromedriver'

#secretモード
options=Options()
options.add_argument("--incognito")

driver=webdriver.Chrome(executable_path=chrome_path,options=options)
url="https://search.yahoo.co.jp/image"
driver.get(url)

sleep(3)

# 検索とスクロール
word="チャンピオンズリーグ優勝"
search_box=driver.find_element_by_class_name('SearchBox__searchInput')
search_box.send_keys(word)
search_box.submit()

sleep(3)

height=1000
while height<10000:
    #scrollTo(x座標、y座標)
    driver.execute_script("window.scrollTo(0,{});".format(height))
    height+=100

    sleep(1)

#画像の要素を選択
elements=driver.find_elements_by_class_name('sw-ThumbnailGrid__row')

#list作成
list=[]

#要素から取得
for i,element in enumerate (elements,start=1):
    name=f'{word}_{i}'
    img_url=element.find_element_by_tag_name("img").get_attribute("src")
    origin=element.find_element_by_class_name("sw-ThumbnailGrid__details").get_attribute("href")
    title=element.get_attribute("textContent")

    d={
        "name": name,
        "img_url": img_url,
        "origin": origin,
        "title":title
    }

    list.append(d)

    sleep(1)

df=pd.DataFrame(list)
df.to_csv("champions_league_v.csv")

driver.quit()
