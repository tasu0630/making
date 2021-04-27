from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

chrome_path = '/Users/tasuke0630/making/scraping/chromedriver'

options=Options()
options.add_argument("--incognito")

driver=webdriver.Chrome(executable_path=chrome_path,options=options)
url="https://www.mizuhobank.co.jp/retail/takarakuji/loto/backnumber/detail.html?fromto=1_400&type=loto7"
driver.get(url)

sleep(3)

height=0
while height<20000:
    driver.execute_script("window.scrollTo(70,{});".format(height))
    height+=1000

    sleep(2)

#要素を選択
elements= driver.find_elements_by_class_name("js-lottery-backnumber-temp-pc")

#list、変数の作成
td=[0,1,2,3,4,5,6,]
t_list=[]
i=1

#要素から取得
for i,element in enumerate (elements,start=1):
    #name=element.find_element_by_tag_name("th").get_attribute("textContent")

    td[0]=element.find_elements_by_tag_name("td")[1].get_attribute("textContent")
    td[1]=element.find_elements_by_tag_name("td")[2].get_attribute("textContent")
    td[2]=element.find_elements_by_tag_name("td")[3].get_attribute("textContent")
    td[3]=element.find_elements_by_tag_name("td")[4].get_attribute("textContent")
    td[4]=element.find_elements_by_tag_name("td")[5].get_attribute("textContent")
    td[5]=element.find_elements_by_tag_name("td")[6].get_attribute("textContent")
    td[6]=element.find_elements_by_tag_name("td")[7].get_attribute("textContent")

    for j in range(7):
        tmp={
            "number":td[j],
        }

    #result_table
    # tmp={
        #"name":name,
        #"number1":list_td[0],
        #"number2":list_td[1],
        #"number3":list_td[2],
        #"number4":list_td[3],
        #"number5":list_td[4],
        #"number6":list_td[5],
        #"number7":list_td[6]
    #}

        t_list.append(tmp)

    sleep(1)

df=pd.DataFrame(t_list)
df.to_csv("loto7_detail.csv")


driver.quit()
