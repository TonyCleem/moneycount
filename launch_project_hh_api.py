import requests
import pprint


def get_rub_salary(vacansies_name):
    url = 'https://api.hh.ru/vacancies'
    payload = {"text": f"{vacansies_name}", 'area': '1',}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    rub_salary = response.json()
    return rub_salary


def get_vacansies_statistic(vacancies_found, vacancies_processed, average_salary):
    vacansies_statistic = {}
    vacansies_statistic['vacancies_found'] = vacancies_found
    vacansies_statistic['vacancies_processed'] = vacancies_processed
    vacansies_statistic['average_salary'] = average_salary
    return vacansies_statistic


def get_average_salary(salaries):
    average_salary = []
    for salary in salaries:
        programmer_salary = salary['salary']
        if not programmer_salary:
            continue
        for money in programmer_salary.keys():
            if money != 'from':
                continue
            if not programmer_salary[money]:
                continue
            programmer_salary = programmer_salary[money] * 1.2
            average_salary.append(programmer_salary)
    average_salary = sum(average_salary) / len(average_salary)
    average_salary = round(average_salary)
    return average_salary


def get_vacancies_processed(salaries):
    vacancies_processed = 0
    for salary in salaries:
        programmer_salary = salary['salary']
        if not programmer_salary:
            continue
        for money in programmer_salary.keys():
            if money != 'from':
                continue
            vacancies_processed += 1
    return vacancies_processed


if __name__ == '__main__':
    vacansies_name = ['Python', 'Java', 'Ruby', 'PHP']
    predict_rub_salary = {}
    for vacansy in vacansies_name:
        rub_salary = get_rub_salary(vacansy)
        salaries = rub_salary['items']

        vacancies_found = rub_salary['found']
        vacancies_processed = get_vacancies_processed(salaries)
        average_salary = get_average_salary(salaries)

        vacansies_statistic = get_vacansies_statistic(vacancies_found, vacancies_processed, average_salary)
        predict_rub_salary[f'{vacansy}'] = vacansies_statistic

    pprint.pprint(predict_rub_salary)



 


    





 





      
         

