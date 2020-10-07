import requests
from itertools import count
import os
from dotenv import load_dotenv


def average_predict_rub_salary_per_page_hh(programming_language, page=0):

    url = f'https://api.hh.ru/vacancies'
    params = {
        'text': f'Программист{programming_language}',
        'period':'30',
        'area' : '1',
        'page' : page
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    sum_salary, error, predict_salary, vacancy_index = 0,0,0,0
    for vacancy_index, vacancy_json in enumerate(response.json()['items']):
        try:
            lower_salary = response.json()['items'][vacancy_index]['salary']['from']
            top_salary = response.json()['items'][vacancy_index]['salary']['to']
            currency = response.json()['items'][vacancy_index]['salary']['currency']
            predict_salary, error = calculate_predict_salary(currency, lower_salary, top_salary,'RUR', error)
            sum_salary = sum_salary + predict_salary
        except TypeError:
            error = error + 1
    number_of_pages = response.json()['pages']
    vacancy_numbers_per_page = vacancy_index + 1 - error
    vacancies_found = response.json()['found']
    if vacancy_numbers_per_page == 0:
        average_salary_per_page = 0
    else:
        average_salary_per_page = int(sum_salary/(vacancy_numbers_per_page))
    return (vacancy_numbers_per_page, average_salary_per_page, number_of_pages, vacancies_found)


def average_predict_rub_salary(function_average_predict_rub_salary_per_page, programming_language):

    vacancies_processed = 0
    sum_predict_rub_salary_all_pages = 0
    for page in count(0):
        vacancy_numbers_per_page, average_salary_per_page, number_of_pages, vacancies_found = function_average_predict_rub_salary_per_page(programming_language, page)
        sum_predict_rub_salary_all_pages = sum_predict_rub_salary_all_pages + average_salary_per_page
        vacancies_processed = vacancies_processed + vacancy_numbers_per_page
        if page >= (number_of_pages-1):
            break
    average_salary_all_pages = int(sum_predict_rub_salary_all_pages/(page+1))
    return vacancies_found, vacancies_processed, average_salary_all_pages


def average_predict_rub_salary_per_page_sj(programming_language, page = 0 ):

    url = 'https://api.superjob.ru/2.33/vacancies/'
    headers = {'X-Api-App-Id': f'{super_job_secret_key}'}
    params = {
        'catalogues': '48',
        'town': '4',
        'page' : page,
        'keyword': f'{programming_language}'
    }
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    response.json()
    sum_salary, error, predict_salary, vacancy_index= 0,0,0,0
    for vacancy_index, vacancy_json in enumerate(response.json()['objects']):
        lower_salary = response.json()['objects'][vacancy_index]['payment_from']
        top_salary = response.json()['objects'][vacancy_index]['payment_to']
        currency = response.json()['objects'][vacancy_index]['currency']
        predict_salary, error = calculate_predict_salary(currency, lower_salary, top_salary, 'rub', error)
        sum_salary = sum_salary + predict_salary
    number_of_pages = (response.json()['total']//20+1)
    vacancy_numbers_per_page = vacancy_index + 1 - error
    vacancies_found = response.json()['total']
    if vacancy_numbers_per_page == 0:
        average_salary_per_page = 0
    else:
        average_salary_per_page = int(sum_salary/(vacancy_numbers_per_page))
    return (vacancy_numbers_per_page, average_salary_per_page, number_of_pages, vacancies_found)


def calculate_predict_salary(currency, lower_salary, top_salary, valid_currency, error = 0):

        predict_salary = 0
        if currency != valid_currency or (top_salary == 0 and lower_salary == 0):
            error = error +1
        elif top_salary == 0 or top_salary == None: predict_salary = lower_salary*1.2
        elif lower_salary == 0 or lower_salary == None: predict_salary = top_salary*0.8
        else: predict_salary = (lower_salary+top_salary)/2
        return predict_salary, error

if __name__ == '__main__':

    load_dotenv()
    super_job_secret_key = os.getenv("SUPER_JOB_SECRET_KEY")


    try:
          javascript_1, javascript_2, javascript_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_hh, 'Javascript')
          java_1, java_2, java_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_hh, 'Javascript')
          python_1, python_2, python_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_hh, 'Python')
          ruby_1, ruby_2, ruby_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_hh, 'Ruby')
          php_1, php_2,php_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_hh, 'PHP')
          scala_1, scala_2, scala_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_hh, 'Scala')
          c_1, c_2, c_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_hh, 'C')
          shell_1, shell_2, shell_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_hh, 'Shell')

          average_salary_of_vacancies_all_pages_hh = {
            'Javascript':{'vacancies_found':javascript_1, "vacancies_processed": javascript_2, "average_salary":javascript_3},
            'Java':{'vacancies_found':java_1, "vacancies_processed": java_2, "average_salary":java_3},
            'Python':{'vacancies_found':python_1, "vacancies_processed": python_2, "average_salary":python_3},
            'Ruby':{'vacancies_found':ruby_1, "vacancies_processed": ruby_2, "average_salary":ruby_3},
            'PHP':{'vacancies_found':php_1, "vacancies_processed": php_2, "average_salary":php_3},
            'Scala':{'vacancies_found':scala_1, "vacancies_processed": scala_2, "average_salary":scala_3},
            'C':{'vacancies_found':c_1, "vacancies_processed": c_2, "average_salary":c_3},
            'Shell':{'vacancies_found':shell_1, "vacancies_processed": shell_2, "average_salary":shell_3}
            }
          javascript_1, javascript_2, javascript_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_sj, 'Javascript')
          java_1, java_2, java_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_sj, 'Javascript')
          python_1, python_2, python_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_sj, 'Python')
          ruby_1, ruby_2, ruby_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_sj, 'Ruby')
          php_1, php_2,php_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_sj, 'PHP')
          scala_1, scala_2, scala_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_sj, 'Scala')
          c_1, c_2, c_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_sj, 'C')
          shell_1, shell_2, shell_3 = average_predict_rub_salary(average_predict_rub_salary_per_page_sj, 'Shell')

          average_salary_of_vacancies_all_pages_sj = {
          'Javascript':{'vacancies_found':javascript_1, "vacancies_processed": javascript_2, "average_salary":javascript_3},
          'Java':{'vacancies_found':java_1, "vacancies_processed": java_2, "average_salary":java_3},
          'Python':{'vacancies_found':python_1, "vacancies_processed": python_2, "average_salary":python_3},
          'Ruby':{'vacancies_found':ruby_1, "vacancies_processed": ruby_2, "average_salary":ruby_3},
          'PHP':{'vacancies_found':php_1, "vacancies_processed": php_2, "average_salary":php_3},
          'Scala':{'vacancies_found':scala_1, "vacancies_processed": scala_2, "average_salary":scala_3},
          'C':{'vacancies_found':c_1, "vacancies_processed": c_2, "average_salary":c_3},
          'Shell':{'vacancies_found':shell_1, "vacancies_processed": shell_2, "average_salary":shell_3}
          }

          print(average_salary_of_vacancies_all_pages_hh)
          print(average_salary_of_vacancies_all_pages_sj)

    except requests.exceptions.HTTPError as error:
          exit("Can't get data from server:\n{0}".format(error))
