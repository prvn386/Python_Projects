import requests

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='

city = input('City name:')

url = api_address + city

json_data = requests.get(url).json()

formatted_data = json_data['weather'][0]['main']
temp = json_data['main']['temp_max']

print(json_data)
print(formatted_data)
print(temp)