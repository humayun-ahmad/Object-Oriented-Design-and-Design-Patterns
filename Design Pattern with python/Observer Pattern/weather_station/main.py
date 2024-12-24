# main.py

from weather_station import WeatherStation
from observer import TemperatureDisplay


weather_station = WeatherStation()

display1 = TemperatureDisplay("Display 1")
display2 = TemperatureDisplay("Display 2")

weather_station.attach(display1)
weather_station.attach(display2)

weather_station.set_temperature(25)
weather_station.set_temperature(30)

weather_station.detach(display1)

weather_station.set_temperature(35)
