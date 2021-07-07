import cv2
import os

print("フォルダにある画像を使いますか？/yes or no")
answer=input()

if answer=="no":
    os.system("fswebcam -d /dev/video0 -r 640x480 fsw.jpg")
    jpg="fsw.jpg"

elif answer=="yes":
    print("指定する画像ファイルの名前を入力してください。（ファイル形式はjpgのみ対応）")
    print("例 x.jpg")
    jpg=input()

else:
    print("yesかnoかで答えてください。")
    exit()


    
count_x=0

faceCascade = cv2.CascadeClassifier('./opencv-master/data/haarcascades/haarcascade_frontalface_default.xml')

faceCascade2 = cv2.CascadeClassifier('./opencv-master/data/haarcascades/haarcascade_smile.xml')

img = cv2.imread(jpg)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
faces = faceCascade.detectMultiScale(gray)


if len(faces)==0:
    print("you are not human!")

else:    
    smile = faceCascade2.detectMultiScale(gray,scaleFactor=2.39,minNeighbors=9)
    for (x, y, w, h) in smile:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0),2)
        count_x+=1

    if count_x>=2:
        print("最高の笑顔!")

    elif count_x==1:
        print("笑顔だけどもっと笑える！")

    else:
        print("笑ってない...")

    name='judgement_' + jpg    
    cv2.imwrite(name,img)
