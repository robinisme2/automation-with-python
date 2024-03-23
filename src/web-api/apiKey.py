import requests, json
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'appid': 'xxx', id='12345'}
response = requests.get(baseUrl, params=parameters)
print(response.content)