import requests


programming_languages = ['PHP', 'Ruby', 'Python', 'Java', 'JavaScript']
found = {}
for programming_language in programming_languages:
    url = 'https://api.hh.ru/vacancies'
    payload = {"text": f"{programming_language}",
    'area': '1',
    }
    
    response = requests.get(url, params=payload)
    print(response.url)
    response.raise_for_status()
    vacansies = response.json()
    salares = vacansies['items'][1]['salary']
    print(salares)
        # more_salares['from'] = salary['from']
        # more_salares['to'] = salary['to']
        # more_salares['currency'] = salary['currency']
        # more_salares['gross'] = salary['gross']






