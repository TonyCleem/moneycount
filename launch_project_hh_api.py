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


def get_average_salary(all_vacancies):
    average_salary = []
    for salary in all_vacancies:
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
            count + 1
    average_salary = round(sum(average_salary)) / round(len(average_salary))


# def get_vacancies_processed(all_vacancies):
#     vacancies_processed = 0
#     for salary in all_vacancies:
#         if salary['id']:
#             vacancies_processed +=1
#     return vacancies_processed

    


if __name__ == '__main__':
    predict_rub_salary = {}
    page = 2
    pages = 3
    url = 'https://api.hh.ru/vacancies'
    vacansies_name = ['Python', 'Java']
    
    
    
    for vacansy in vacansies_name:
        while page < pages:
            page_response = requests.get(url, params={'page': page,"text": f"{vacansy}", 'area': '1'})
            page_response.raise_for_status()
            page_payload = page_response.json()
        

            all_vacancies = page_payload['items']
            average_salary = []
            count = 0
            for salary in all_vacancies:
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
                    count + 1
        page +=1
        average_salary = sum(average_salary) / len(average_salary)
        average_salary = round(average_salary)
        print(average_salary)

        print(count)
     # vacancies_found = page_payload['found']
        # all_vacancies = page_payload['items']
        # average_salary = get_average_salary(all_vacancies)
        # vacansies_statistic = get_vacansies_statistic(vacancies_found, vacancies_processed, average_salary)
        # predict_rub_salary[f'{vacansy}'] = vacansies_statistic  
    # pprint.pprint(predict_rub_salary)