#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tkinter as tk
from tkinter import ttk
import requests

def get_weather():
    city = city_entry.get()
    unit = unit_var.get()
    api_key = '0eb523a6d7d9e5674b059e73512726f5'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units={unit}&appid={api_key}'

    try:
        response = requests.get(url)
        data = response.json()
        weather_info.set(f'Temperature: {data["main"]["temp"]}°{unit}\nHumidity: {data["main"]["humidity"]}%\nWind Speed: {data["wind"]["speed"]} {unit}')
    except Exception as e:
        weather_info.set(f'Error fetching data: {e}')
app = tk.Tk()
app.title("Weather App")
app.geometry("400x300")
title_label = ttk.Label(app, text="Weather App", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

city_label = ttk.Label(app, text="Enter City:")
city_label.pack()

city_entry = ttk.Entry(app)
city_entry.pack(pady=5)

unit_var = tk.StringVar()
unit_label = ttk.Label(app, text="Choose Unit:")
unit_label.pack()

unit_menu = ttk.OptionMenu(app, unit_var, "metric", "metric", "imperial")
unit_menu.pack(pady=5)

weather_info = tk.StringVar()
result_label = ttk.Label(app, textvariable=weather_info, font=("Helvetica", 10))
result_label.pack(pady=10)

get_weather_button = ttk.Button(app, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

# Run the application
app.mainloop()


# In[ ]:




