# get data from openweathermap.org through an api as json. Format and display the requested data

import requests
from datetime import datetime

location=input("Enter a city name: ")
api="xyz"
complete_api_link= f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api}"

api_link=requests.get(complete_api_link)
api_data=api_link.json()

if api_data['cod']=='404':
    print(f"Invalid city : {location}. Please check your city name")
else:
    temp_city=((api_data['main']['temp']-273.15))
    weather_desc=api_data['weather'][0]['description']
    hmdt=api_data['main']['humidity']
    wind_speed=api_data['wind']['speed']
    date_time=datetime.now().strftime("%d %b %Y | %I : %M : %S %p")

    print("=========================================================")
    print(f"Weather Stats for - {location.upper()} || {date_time}")
    print("=========================================================")

    print(f"Temperature is : {temp_city:.2f} deg C")
    print(f"City Description : {weather_desc}")
    print(f"Humidity : {hmdt} %")
    print(f"Wind Speed : {wind_speed} kmph")
