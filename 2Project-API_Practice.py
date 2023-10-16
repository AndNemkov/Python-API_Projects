import requests

headers = {"Content-Type":"application/json", "User-agent":"Mozilla"}
api_key = input("Enter a valid API key: ")

country_code = 'US'
zip_code = input("Enter zip code: ")

myURL = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},{country_code}&appid={api_key}'
results = requests.get(myURL, headers=headers)
myJSON = results.json()

print(f"The call returned code {results.status_code}")

print(f"The city name for {zip_code} is {myJSON['name']}")
print(f"The latitude for {zip_code} is {myJSON['lat']}")
print(f"The longitude for {zip_code} is {myJSON['lon']}")
