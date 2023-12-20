import requests

api_key = "478168605be7da4b620e81d4c96a91e5"


def get_data(place, forcast_days=None):
    url = (f"http://api.openweathermap.org/data/2.5/forecast"
           f"?q={place}&appid={api_key}")
    response = requests.get(url)
    data = response.json()
    # Convert into list, so we can access data in that json file
    filtered_data = data["list"]

    # 3 hours of interval so its 40 length
    # So 24hours divided by 3 interval hours is 8 data points
    # And we show user 5 days of data so 8 * 5 is 40 that the logic
    number_value = 8 * forcast_days
    # Zero to number of value that selected in slide bar 1 to 5
    filtered_data = filtered_data[:number_value]
    return filtered_data


# Its's only execute main class or redirect to main class
if __name__ == "__main__":
    print(get_data(place="Tokyo",forcast_days=3))
