# APIリクエストに必要なライブラリ
import requests
import json


# URL＋クエリパラメータ
url = 'http://weather.livedoor.com/forecast/webservice/json/v1?city=400040'
# APIリクエストを送信
tenki_data = requests.get(url).json()

print(tenki_data)



# 「今日」のデータを指定
# print(tenki_data['forecasts'][0])
# # 予報日
# print('予報日：', tenki_data['forecasts'][0]['dateLabel'])
# # 天気
# print('天気：', tenki_data['forecasts'][0]['telop'])