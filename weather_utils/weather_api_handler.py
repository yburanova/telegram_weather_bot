import requests
import constants.constants as const


class WeatherOpenApiHandler:

    def __init__(self):
        self.url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_forecast(self, lat, lon):

        query_params = {
            'lat': lat,
            'lon': lon,
            'appid': const.WEATHER_OPENAPI_TOKEN,
            'lang': 'de',
            'units': 'metric'  # For temperature in Celsius
        }

        response = requests.get(self.url, query_params)

        print(response.json())

        return "Wetter in Bobingen für heute: "
