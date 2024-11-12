import requests
import pprint

url = 'https://api.hh.ru/vacancies'
payload = {'professional_role':'96',
           'area':'113'}

response = requests.get(url, params=payload)


response.raise_for_status()


pprint.pprint(response.json())


