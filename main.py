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
                predicted_salary = calculate_predicted_salary(
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
    average_salary = int(sum(salaries) / vacancies_processed)
    return vacancies_found, vacancies_processed, average_salary


def predict_average_rub_salary_sj(programming_language):

    salaries = []
    for page in count(0):
        url = 'https://api.superjob.ru/2.33/vacancies/'
        headers = {'X-Api-App-Id': os.getenv("SUPER_JOB_SECRET_KEY")}
        params = {
            'catalogues': '48',
            'town': '4',
            'page': page,
            'keyword': programming_language
        }
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        resp = response.json()
        vacancies = resp['objects']
        for vacancy_number, vacancy in enumerate(vacancies):
            lower_salary = vacancies[vacancy_number]['payment_from']
            top_salary = vacancies[vacancy_number]['payment_to']
            currency = vacancies[vacancy_number]['currency']
            predicted_salary = calculate_predicted_salary(
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
    average_salary = int(sum(salaries)/vacancies_processed)
    return vacancies_found, vacancies_processed, average_salary


def calculate_predicted_salary(
        currency, lower_salary, top_salary, valid_currency):

    predicted_salary = 0
    if currency != valid_currency or (top_salary == 0 and lower_salary == 0):
        pass
    elif not top_salary:
        predicted_salary = lower_salary*1.2
    elif not lower_salary:
        predicted_salary = top_salary*0.8
    else:
        predicted_salary = (lower_salary+top_salary)/2
    return predicted_salary


def display_the_average_salary_in_table_form(programming_languages,
                                             title,
                                             predict_salary_function):

    table_headers =[
        ('Programming language',
        'Vacancies found',
        'Vacancies processed',
        'Average salary')
    ]

    table_rows = []
    for language_index, programming_language in enumerate(programming_languages):
        vacancies_found, vacancies_processed, average_salary = \
            predict_salary_function(programming_language)
        table_rows.append((programming_language,
                           vacancies_found,
                           vacancies_processed,
                           average_salary))

    table = tuple(table_headers + table_rows)
    table_instance = AsciiTable((table), title)
    table_instance.justify_columns[3] = 'right'
    print(table_instance.table)


if __name__ == '__main__':

    load_dotenv()

    try:

        programming_languages = [
            'Javascript',
            'Java',
            'Python',
            'Ruby',
            'PHP',
            'Scala',
            'C',
            'C++'
        ]

        display_the_average_salary_in_table_form(
            programming_languages,
            'SuperJob Moscow',
            predict_average_rub_salary_sj)
        display_the_average_salary_in_table_form(
            programming_languages,
            'HeadHunter Moscow',
            predict_average_rub_salary_hh)

    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))
