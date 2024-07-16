import requests
import json
# from pprint import pprint

TOKEN = '302cd93571f7e72c3dba77940967b189'
city_name = input("Input the city: ")

def get_weather(city_name, TOKEN):
    try:
        converter = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={TOKEN}")
        jsconv = converter.json()
        if len(jsconv) > 0:
            data = jsconv[0]
            _lat = data['lat']
            _lon = data['lon']
            
            weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={_lat}&lon={_lon}&appid={TOKEN}&units=metric")
            weatherconv = weather.json()
            _temp = weatherconv['main']['temp']
            print(str(int(round(_temp, 0))) + "°C")
        else:
            print("Wrong name for the city! Try again!")
        
    except Exception as ex:
        print(ex)
        print("Wrong name for the city! Try again!")

get_weather(city_name, TOKEN)

