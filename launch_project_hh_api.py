import requests
import pprint

def get_predict_rub_salary(vacansies_name):
    url = 'https://api.hh.ru/vacancies'
    payload = {"text": f"{vacansies_name}", 'area': '1',}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    predict_rub_salary = response.json()
    return predict_rub_salary
    

if __name__ == '__main__':
    vacansies_name = 'JavaScript'
    get_predict_rub_salary = get_predict_rub_salary(vacansies_name)

    vacancies_salary = get_predict_rub_salary['items']
    for salary in vacancies_salary:
        salary_amounts = salary['salary']
        if not salary_amounts:
            print(None)
            continue
        for salary_amount in salary_amounts.keys():
            if salary_amount != 'from':
                continue
            print(salary_amounts[salary_amount])
