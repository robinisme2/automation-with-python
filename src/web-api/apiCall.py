import requests, json
# url: https://www.upcitemdb.com/api/explorer#!/lookup/get_trial_lookup?upc=xxxx
baseUrl = 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '012993441012'}
response = requests.get(baseUrl, params=parameters)
print(response.url)

content = response.content
info = json.loads(content)
print(type(info))
print(info)