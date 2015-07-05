# -*- coding: utf-8 -*-
import urllib
import requests
import json

def get_weather_data():
    city = input('请输入要查询的城市：')
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city
    weather_data = requests.get(url).text
    weather_dict = json.loads(weather_data)
    if weather_dict.get('desc') == 'OK':
        print('城市：' + weather_dict.get('data').get('city'))
        print('温度：' + weather_dict.get('data').get('wendu') + '℃')
        print('感冒：' + weather_dict.get('data').get('ganmao'))
        print('风向：' + weather_dict.get('data').get('forecast')[0].get('fengxiang'))
        print('风级：' + weather_dict.get('data').get('forecast')[0].get('fengli'))
        print('高温：' + weather_dict.get('data').get('forecast')[0].get('high'))
        print('低温：' + weather_dict.get('data').get('forecast')[0].get('low'))
        print('天气：' + weather_dict.get('data').get('forecast')[0].get('type'))
        print('日期：' + weather_dict.get('data').get('forecast')[0].get('date'))
        print('*' * 50)
        key = input('是否显示未来四天的天气情况？（Y/N）')
        if key == 'Y' or 'y':
            for i in range(1, 5):
                print('日期：' + weather_dict.get('data').get('forecast')[i].get('date'))
                print('风向：' + weather_dict.get('data').get('forecast')[i].get('fengxiang'))
                print('风级：' + weather_dict.get('data').get('forecast')[i].get('fengli'))
                print('高温：' + weather_dict.get('data').get('forecast')[i].get('high'))
                print('低温：' + weather_dict.get('data').get('forecast')[i].get('low'))
                print('天气：' + weather_dict.get('data').get('forecast')[i].get('type'))
                print('-' * 50)
    else:
        print('您输入的城市有误，或者天气中心未收录您输入的城市。')

get_weather_data()
