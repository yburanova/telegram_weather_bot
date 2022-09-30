from weather_utils.weather_api_handler import WeatherOpenApiHandler
from geopy.geocoders import Nominatim
import datetime

class WeatherService:

    def __init__(self):
        self.api_handler = WeatherOpenApiHandler()

    def get_weather_for_city(self, city_name):

        lat, lon = self.get_coordinates_from_cityname(city_name)

        weather_json = self.api_handler.get_forecast(lat, lon)

        print(weather_json)
        weather_map = {}
        print(weather_json['weather'])

        weather_map['place'] = weather_json['name']
        weather_map['country'] = weather_json['sys']['country']
        weather_map['description_icon'] = weather_json['weather'][0]['icon']
        weather_map['description'] = weather_json['weather'][0]['description']
        weather_map['temperature_now'] = weather_json['main']['temp']
        weather_map['temperature_feels'] = weather_json['main']['feels_like']
        weather_map['humidity'] = weather_json['main']['humidity']
        weather_map['wind_speed'] = weather_json['wind']['speed']

        return self.get_formatted_text(weather_map)

    def get_coordinates_from_cityname(self, cityname):
        app = Nominatim(user_agent="weather_telegram_bot")

        geocode_results = app.geocode(cityname)

        return geocode_results.latitude, geocode_results.longitude

    def get_formatted_text(self, weather_map):

        weather_smiley = self.get_smiley(weather_map['description_icon'])

        return f"Wetter in {weather_map['place']}, {weather_map['country']} jetzt: \n" \
               f"{weather_smiley} {weather_map['description']} \n" \
               f"\U0001F321 Temperatur: {weather_map['temperature_now']}°C, " \
               f"gefühlt: {weather_map['temperature_feels']}°C \n" \
               f"\U0001F4A6 Luftfeuchtigkeit: {weather_map['humidity']}% \n" \
               f"\U0001F32C Wind: {weather_map['wind_speed']} km/h"

    def get_smiley(self, text):
        icon_map = {
            '01d': '\U0001F31D',  # clear sky, day
            '01n': '\U0001F30C',  # clear sky, night
            '02d': '\U000026C5',  # few clouds
            '02n': '\U000026C5',  # few clouds
            '03d': '\U00002601',  # clouds
            '03n': '\U00002601',  # clouds
            '04d': '\U00002601',  # clouds
            '04n': '\U00002601',  # clouds
            '09d': '\U0001F327',  # shower rain
            '09n': '\U0001F327',  # shower rain
            '10d': '\U0001F326',  # rain
            '10n': '\U0001F326',  # rain
            '11d': '\U0001F329',  # rain
            '11n': '\U0001F329',  # rain
            '13d': '\U00002744',  # rain
            '13n': '\U00002744',  # rain
            '50d': '\U0001F32B',  # rain
            '50n': '\U0001F32B',  # rain
        }

        return icon_map.get(text, '')
