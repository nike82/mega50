import requests

# API_KEY = "10b900c803e1c290786cb47fa6066504"
API_KEY = "141710af2113bab9f55ef73e1bcd33d5"


def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    number_values = 8 * forecast_days
    filtered_data = filtered_data[:number_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Oslo", forecast_days=3))
