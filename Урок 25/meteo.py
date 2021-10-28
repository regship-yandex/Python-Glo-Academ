import requests
apikey = 'ec8aeea39bd5ba8bf3f62a90e3123852'
units = 'metric'
city = 'Москва'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units={units}'

r = requests.get(url)
print(r.json()['main']['temp'])
