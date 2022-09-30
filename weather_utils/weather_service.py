from weather_utils.weather_api_handler import WeatherOpenApiHandler
from geopy.geocoders import Nominatim


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
        return f"Wetter in {weather_map['place']}, {weather_map['country']} jetzt: \n" \
               f"{weather_map['description']} \n" \
               f"Temperatur: {weather_map['temperature_now']}°C \n" \
               f"gefühlt: {weather_map['temperature_feels']}°C \n" \
               f"Luftfeuchtigkeit: {weather_map['humidity']}% \n" \
               f"Wind: {weather_map['wind_speed']} km/h"
