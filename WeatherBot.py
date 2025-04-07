import requests

api_key = '1af0a5b3527093545dab06c3b2899295'
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city = input("Enter city name: ")

complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"

response = requests.get(complete_url)

data = response.json()

if data["cod"] == "404":
    print("City not found!")
else:
    main = data["main"]
    weather = data["weather"][0]
    wind = data["wind"]

    print(f"\nWeather in {city}:")
    print(f"Temperature: {main['temp']}°C")
    print(f"Humidity: {main['humidity']}%")
    print(f"Weather: {weather['description']}")
    print(f"Wind Speed: {wind['speed']} m/s")
