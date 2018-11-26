# -*- coding: utf-8 -*-
import urllib.request
import json

class WeatherHacks(object):
    def __init__(self, cityid):
        self.cityid = cityid
        # weather hacks からの文字の読み込み，クラス内変数 wstring に保持
        src = "http://weather.livedoor.com/forecast/webservice/json/v1?city=%s"
        f = urllib.request.urlopen(src % (cityid))
        data = f.read()
        f.close()
        w = json.loads(data)
        self.city = w["location"]["city"]
        self.wstring = w
        

    def Forecast(self, day='today'):
       # すでに保持されている wstring を解析することで天気を予報
        w = self.wstring
        if day == "today":
            d = 0
        elif day == "tomorrow":
            d = 1
        self.weather = w["forecasts"][d]["telop"]
        return self.city+"地方の天気: "+self.weather

    def Description(self):
       # すでに保持されている wstring を解析することで概況を表示
        w = self.wstring
        self.description = w["description"]["text"]
        return self.description


# テストコード
Kurume = WeatherHacks('400040')
Tokyo = WeatherHacks('130010')

print(Kurume.Forecast())
print(Tokyo.Forecast(day='tomorrow'))
print(Tokyo.Description())