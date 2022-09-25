from weather_utils.weather_api_handler import WeatherOpenApiHandler


class WeatherService:

    def __init__(self):
        self.api_handler = WeatherOpenApiHandler()

    def get_weather_for_city(self, city_name):

        lat = '48.266667'
        lon = '10.816667'

        return self.api_handler.get_forecast(lat, lon)
