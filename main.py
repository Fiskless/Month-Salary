import requests
from datetime import datetime, timedelta
from itertools import count


def get_fresh_vacancies_from_moscow(url):

    response = requests.get(url)
    response.raise_for_status()

    date_month_ago = (datetime.now()-timedelta(days=31))
    for vacancy_index, hh_json in enumerate(response.json()['items']):
        date_of_publication = (response.json()['items'][vacancy_index]['published_at'])
        if response.json()['items'][vacancy_index]['area']['name'] == "Москва" and (int(date_of_publication [0:4]), int(date_of_publication [6:7]),int(date_of_publication [8:10])) > (int(date_month_ago.year),int(date_month_ago.month),int(date_month_ago.day)):
            print(response.json()['items'][vacancy_index])



def count_the_number_of_vacancies(programming_language):
    url = f'https://api.hh.ru/vacancies?text=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82%20{programming_language}'
    response = requests.get(url)
    response.raise_for_status()

    return response.json()['found']


def get_salary_from_vacancies(url):

    response = requests.get(url)
    response.raise_for_status()

    for vacancy_index, vacancy_json in enumerate (response.json()['items']):
        print(vacancy_index, response.json()['items'][vacancy_index]['salary'])

def average_predict_rub_salary(programming_language):

    url = f'https://api.hh.ru/vacancies?text=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82%20{programming_language}'
    response = requests.get(url)
    response.raise_for_status()
    sum_salary = 0
    for vacancy_index, vacancy_json in enumerate (response.json()['items']):
        try:
            lower_salary = response.json()['items'][vacancy_index]['salary']['from']
            top_salary = response.json()['items'][vacancy_index]['salary']['to']
            currency = response.json()['items'][vacancy_index]['salary']['currency']
            if currency != 'RUR':predict_salary = 'None'
            elif top_salary == None: predict_salary = lower_salary*1.2
            elif lower_salary == None: predict_salary = top_salary*0.8
            else: predict_salary = (lower_salary+top_salary)/2
            # print(predict_salary)
            sum_salary = sum_salary + predict_salary
        except TypeError:
            # print(None)
            predict_salary = 0
    return ((vacancy_index+1), int(sum_salary/(vacancy_index+1)))

def download_all_pages(url):
    for page in count(0):
        page_response = requests.get(url, params={'page': page})
        page_response.raise_for_status()

        page_data = page_response.json()

        print(page_data)
        if page >= page_data['pages']:
            break

if __name__ == '__main__':

    # get_fresh_vacancies_from_moscow('https://api.hh.ru/vacancies?text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82%20Python')
    # #


    # get_salary_from_vacancies('https://api.hh.ru/vacancies?text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82%20Python')
    #
    # predict_rub_salary('Python')

    # average_salary_of_vacancies = {
    #     'Javascript':{'vacancies_found':count_the_number_of_vacancies('Javascript'), "vacancies_processed": average_predict_rub_salary('Javascript')[0], "average_salary":average_predict_rub_salary('Javascript')[1]},
    #     'Java':{'vacancies_found':count_the_number_of_vacancies('Java'), "vacancies_processed": average_predict_rub_salary('Java')[0], "average_salary":average_predict_rub_salary('Java')[1]},
    #     'Python':{'vacancies_found':count_the_number_of_vacancies('Python'), "vacancies_processed": average_predict_rub_salary('Python')[0], "average_salary":average_predict_rub_salary('Python')[1]},
    #     'Ruby':{'vacancies_found':count_the_number_of_vacancies('Ruby'), "vacancies_processed": average_predict_rub_salary('Ruby')[0], "average_salary":average_predict_rub_salary('Ruby')[1]},
    #     'PHP':{'vacancies_found':count_the_number_of_vacancies('PHP'), "vacancies_processed": average_predict_rub_salary('PHP')[0], "average_salary":average_predict_rub_salary('PHP')[1]},
    #     'C++':{'vacancies_found':count_the_number_of_vacancies('C++'), "vacancies_processed": average_predict_rub_salary('C++')[0], "average_salary":average_predict_rub_salary('C++')[1]},
    #     'C':{'vacancies_found':count_the_number_of_vacancies('C'), "vacancies_processed": average_predict_rub_salary('C')[0], "average_salary":average_predict_rub_salary('C')[1]},
    #     'Shell':{'vacancies_found':count_the_number_of_vacancies('Shell'), "vacancies_processed": average_predict_rub_salary('Shell')[0], "average_salary":average_predict_rub_salary('Shell')[1]}
    # }
    # print(average_salary_of_vacancies)


    try:
        data = download_all_pages('https://api.hh.ru/vacancies?text=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82%20Python')
    except requests.exceptions.HTTPError as error:
        exit("Can't get data from server:\n{0}".format(error))























