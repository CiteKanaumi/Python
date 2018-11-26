# -*- coding: utf-8 -*-
import urllib.request
import json

# 関数定義部 （ここを書く）
def Forecast(city='400040'):
    src = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s"
    f = urllib.request.urlopen(src % (city))
    data = f.read()
    f.close()
    w = json.loads(data)
    weather = w["forecasts"][0]["dateLabel"]+"の天気は"+w["forecasts"][0]["telop"]+"です."
    return (weather)



# 以下はテストの為のルーチン．
print('\n\n---test1---')
strdat = Forecast(city='400040')
print(strdat)

print('\n\n---test2---')
strdat = Forecast(city='130010')
print(strdat)
