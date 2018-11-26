# -*- coding: utf-8 -*-
import urllib.request
import json

# 関数定義部 （ここを書く）
def Forecast(city='400040', day='today'):
    src = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s"
    f = urllib.request.urlopen(src % (city))
    data = f.read()
    f.close()
    w = json.loads(data)
    if day == "today":
        d = 0
    elif day == "tomorrow":
        d = 1
    weather = w["forecasts"][d]["dateLabel"]+"の天気は"+w["forecasts"][d]["telop"]+"です."

    return (weather)

# 以下はテストの為のルーチン．
print('\n\n---test1---')
strdat = Forecast(city='400040')
print(strdat)

print('\n\n---test2---')
strdat = Forecast(city='400040', day='tomorrow')
print(strdat)

print('\n\n---test3---')
strdat = Forecast(city='130010', day='today')
print(strdat)
