from requests_oauthlib import OAuth1Session , OAuth1
import json
import requests
import urllib
import sys
import tkinter

#tkinterでウィンドウを新規作成
window = tkinter.Tk()
window.title(u'Tweetの投稿')

#APIキー情報設定
consumer_key = "QnGY2Zo5PzMddbIGpSUwrJ4nC"
consumer_key_secret = "XD1SiZp8NvapNEiIthKwfDwKKJzt0JyQq1tYY6O39WgzeIAnyp"
access_token = "1235335223090569220-msalwH8gpFuDHrVEHL1lU9f6gWfdXM"
access_token_secret = "Y8bjnZIQhlfo7gOJDZQ9FCdxnnRClaLLFQGOTm7b5jIML"

#Twitter API アクセス time line 取得
def tweet_post(event):
    word = search_form.get()
    if len(word) !=0:
        url = "https://api.twitter.com/1.1/statuses/update.json?status=" + word
        auth = OAuth1(consumer_key, consumer_key_secret, access_token, access_token_secret)
        response = requests.post(url, auth = auth)
        if response.status_code == 200:
            print("OK")
        else:
            print(response)
            print("Error: %d" % response.status_code)
    else:
        print('入力なし')

#tkinterの入力フォーム作成
search_form = tkinter.Entry()
search_form. insert(tkinter.END,"")
search_form.pack()

#tkinterのツイートボタン作成
tweet_button = tkinter.Button(text = 'tweetする', width=20)
tweet_button.bind("<Button-1>",tweet_post)
tweet_button.pack()

#ウィンドウ表示
window.geometry('400x300')
window.mainloop()
