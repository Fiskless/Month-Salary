import requests
from itertools import count
import os
from dotenv import load_dotenv
from terminaltables import AsciiTable


def predict_average_rub_salary_hh(programming_language):

    salaries = []
    for page in count(0):
        url = 'https://api.hh.ru/vacancies'
        params = {
            'text': f'Программист{programming_language}',
            'period': '30',
            'area': '1',
            'page': page
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        resp = response.json()
        vacancies = resp['items']
        for vacancy_number, vacancy in enumerate(vacancies):
            try:
                lower_salary = vacancies[vacancy_number]['salary']['from']
                top_salary = vacancies[vacancy_number]['salary']['to']
                currency = vacancies[vacancy_number]['salary']['currency']
                predicted_salary = calculate_predict_salary(
                    currency,
                    lower_salary,
                    top_salary,
                    'RUR',
                )
                if predicted_salary != 0:
                    salaries.append(predicted_salary)
            except TypeError:
                pass
        number_of_pages = resp['pages']
        if page >= number_of_pages-1:
            break
    vacancies_found = resp['found']
    vacancies_processed = len(salaries)
    average_salary_all_pages = int(sum(salaries) / vacancies_processed)
    return vacancies_found, vacancies_processed, average_salary_all_pages


def predict_average_rub_salary_sj(programming_language):

    salaries = []
    for page in count(0):
        url = 'https://api.superjob.ru/2.33/vacancies/'
        headers = {'X-Api-App-Id': f'{super_job_secret_key}'}
        params = {
            'catalogues': '48',
            'town': '4',
            'page': page,
            'keyword': f'{programming_language}'
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        resp = response.json()
        vacancies = resp['objects']
        for vacancy_number, vacancy in enumerate(vacancies):
            lower_salary = vacancies[vacancy_number]['payment_from']
            top_salary = vacancies[vacancy_number]['payment_to']
            currency = vacancies[vacancy_number]['currency']
            predicted_salary = calculate_predict_salary(
                currency,
                lower_salary,
                top_salary,
                'rub',
                )
            if predicted_salary != 0:
                salaries.append(predicted_salary)
        number_of_pages = (resp['total'] // 20 + 1)
        if page >= number_of_pages-1:
            break
    vacancies_found = resp['total']
    vacancies_processed = len(salaries)
    average_salary_all_pages = int(sum(salaries)/vacancies_processed)
    return vacancies_found, vacancies_processed, average_salary_all_pages


def calculate_predict_salary(
        currency, lower_salary, top_salary, valid_currency):

    predicted_salary = 0
    if currency != valid_currency or (top_salary == 0 and lower_salary == 0):
        pass
    elif top_salary == 0 or top_salary == None:
        predicted_salary = lower_salary*1.2
    elif lower_salary == 0 or lower_salary == None:
        predicted_salary = top_salary*0.8
    else:
        predicted_salary = (lower_salary+top_salary)/2
    return predicted_salary


def predict_average_salary_in_table_form_all_pages(title, dict_input):

    title = title
    programming_language = list(dict_input.keys())

    table_data = (
        (
            'Programming language',
            'Vacancies found',
            'Vacancies processed',
            'Average salary'
        ),
        (
            programming_language[0],
            dict_input[programming_language[0]]['vacancies_found'],
            dict_input[programming_language[0]]['vacancies_processed'],
            dict_input[programming_language[0]]['average_salary']
        ),
        (
            programming_language[1],
            dict_input[programming_language[1]]['vacancies_found'],
            dict_input[programming_language[1]]['vacancies_processed'],
            dict_input[programming_language[1]]['average_salary']
        ),
        (
            programming_language[2],
            dict_input[programming_language[2]]['vacancies_found'],
            dict_input[programming_language[2]]['vacancies_processed'],
            dict_input[programming_language[2]]['average_salary']
        ),
        (
            programming_language[3],
            dict_input[programming_language[3]]['vacancies_found'],
            dict_input[programming_language[3]]['vacancies_processed'],
            dict_input[programming_language[3]]['average_salary']
        ),
        (
            programming_language[4],
            dict_input[programming_language[4]]['vacancies_found'],
            dict_input[programming_language[4]]['vacancies_processed'],
            dict_input[programming_language[4]]['average_salary']
        ),
        (
            programming_language[5],
            dict_input[programming_language[5]]['vacancies_found'],
            dict_input[programming_language[5]]['vacancies_processed'],
            dict_input[programming_language[5]]['average_salary']
        ),
        (
            programming_language[6],
            dict_input[programming_language[6]]['vacancies_found'],
            dict_input[programming_language[6]]['vacancies_processed'],
            dict_input[programming_language[6]]['average_salary']
        ),
        (
            programming_language[7],
            dict_input[programming_language[7]]['vacancies_found'],
            dict_input[programming_language[7]]['vacancies_processed'],
            dict_input[programming_language[7]]['average_salary']
        )
    )
    table_instance = AsciiTable(table_data, title)
    table_instance.justify_columns[3] = 'right'
    print(table_instance.table)

if __name__ == '__main__':

    load_dotenv()
    super_job_secret_key = os.getenv("SUPER_JOB_SECRET_KEY")

    try:
        js_1, js_2, js_3 = predict_average_rub_salary_hh('Javascript')
        java_1, java_2, java_3 = predict_average_rub_salary_hh('Java')
        python_1, python_2, python_3 = predict_average_rub_salary_hh('Python')
        ruby_1, ruby_2, ruby_3 = predict_average_rub_salary_hh('Ruby')
        php_1, php_2, php_3 = predict_average_rub_salary_hh('PHP')
        scala_1, scala_2, scala_3 = predict_average_rub_salary_hh('Scala')
        c_1, c_2, c_3 = predict_average_rub_salary_hh('C')
        shell_1, shell_2, shell_3 = predict_average_rub_salary_hh('Shell')

        average_salary_of_vacancies_all_pages_hh = {
            'Javascript': {
                'vacancies_found': js_1,
                "vacancies_processed": js_2,
                "average_salary": js_3
            },
            'Java': {
                "vacancies_found": java_1,
                "vacancies_processed": java_2,
                "average_salary": java_3
            },
            'Python': {
                "vacancies_found": python_1,
                "vacancies_processed": python_2,
                "average_salary": python_3
            },
            'Ruby': {
                "vacancies_found": ruby_1,
                "vacancies_processed": ruby_2,
                "average_salary": ruby_3
            },
            'PHP': {
                "vacancies_found": php_1,
                "vacancies_processed": php_2,
                "average_salary": php_3
            },
            'Scala': {
                "vacancies_found": scala_1,
                "vacancies_processed": scala_2,
                "average_salary": scala_3
            },
            'C': {
                "vacancies_found": c_1,
                "vacancies_processed": c_2,
                "average_salary": c_3
            },
            'Shell': {
                "vacancies_found": shell_1,
                "vacancies_processed": shell_2,
                "average_salary": shell_3
            }
        }

        js_1, js_2, js_3 = predict_average_rub_salary_sj('Javascript')
        java_1, java_2, java_3 = predict_average_rub_salary_sj('Java')
        python_1, python_2, python_3 = predict_average_rub_salary_sj('Python')
        ruby_1, ruby_2, ruby_3 = predict_average_rub_salary_sj('Ruby')
        php_1, php_2, php_3 = predict_average_rub_salary_sj('PHP')
        scala_1, scala_2, scala_3 = predict_average_rub_salary_sj('Scala')
        c_1, c_2, c_3 = predict_average_rub_salary_sj('C')
        shell_1, shell_2, shell_3 = predict_average_rub_salary_sj('Shell')

        average_salary_of_vacancies_all_pages_sj = {
            'Javascript': {
                'vacancies_found': js_1,
                "vacancies_processed": js_2,
                "average_salary": js_3
            },
            'Java': {
                "vacancies_found": java_1,
                "vacancies_processed": java_2,
                "average_salary": java_3
            },
            'Python': {
                "vacancies_found": python_1,
                "vacancies_processed": python_2,
                "average_salary": python_3
            },
            'Ruby': {
                "vacancies_found": ruby_1,
                "vacancies_processed": ruby_2,
                "average_salary": ruby_3
            },
            'PHP': {
                "vacancies_found": php_1,
                "vacancies_processed": php_2,
                "average_salary": php_3
            },
            'Scala': {
                "vacancies_found": scala_1,
                "vacancies_processed": scala_2,
                "average_salary": scala_3
            },
            'C': {
                "vacancies_found": c_1,
                "vacancies_processed": c_2,
                "average_salary": c_3
            },
            'Shell': {
                "vacancies_found": shell_1,
                "vacancies_processed": shell_2,
                "average_salary": shell_3
            }
        }

        predict_average_salary_in_table_form_all_pages(
            'SuperJob Moscow',
            average_salary_of_vacancies_all_pages_sj)
        predict_average_salary_in_table_form_all_pages(
            'HeadHunter Moscow',
            average_salary_of_vacancies_all_pages_hh)

    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))
