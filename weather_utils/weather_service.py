from weather_utils.weather_api_handler import WeatherOpenApiHandler
from geopy.geocoders import Nominatim


class WeatherService:

    def __init__(self):
        self.api_handler = WeatherOpenApiHandler()

    def get_weather_for_city(self, city_name):

        lat, lon = self.get_coordinates_from_cityname(city_name)

        return self.api_handler.get_forecast(lat, lon)

    def get_coordinates_from_cityname(self, cityname):
        app = Nominatim(user_agent="weather_telegram_bot")

        geocode_results = app.geocode(cityname)

        return geocode_results.latitude, geocode_results.longitude
