import requests
from datetime import datetime, timedelta, date


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

    for vacancy_index, vacancy_json in enumerate (response.json()['items'], start=1):
        pass
    return vacancy_index


def get_salary_from_vacancies(url):

    response = requests.get(url)
    response.raise_for_status()

    for vacancy_index, vacancy_json in enumerate (response.json()['items']):
        print(vacancy_index, response.json()['items'][vacancy_index]['salary'])

def predict_rub_salary(programming_language):

    url = f'https://api.hh.ru/vacancies?text=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82%20{programming_language}'
    response = requests.get(url)
    response.raise_for_status()

    for vacancy_index, vacancy_json in enumerate (response.json()['items']):
        try:
            lower_salary = response.json()['items'][vacancy_index]['salary']['from']
            top_salary = response.json()['items'][vacancy_index]['salary']['to']
            currency = response.json()['items'][vacancy_index]['salary']['currency']
            if currency != 'RUR':predict_salary = 'None'
            elif top_salary == None: predict_salary = lower_salary*1.2
            elif lower_salary == None: predict_salary = top_salary*0.8
            else: predict_salary = (lower_salary+top_salary)/2
            print(predict_salary)
        except TypeError:
            print(None)




if __name__ == '__main__':

    # get_fresh_vacancies_from_moscow('https://api.hh.ru/vacancies?text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82%20Python')
    #
    # dictionary_of_vacancies = {
    #     'Javascript':count_the_number_of_vacancies('Javascript'),
    #     'Java':count_the_number_of_vacancies('Java'),
    #     'Python':count_the_number_of_vacancies('Python'),
    #     'Ruby':count_the_number_of_vacancies('Ruby'),
    #     'PHP':count_the_number_of_vacancies('PHP'),
    #     'C++':count_the_number_of_vacancies('C++'),
    #     'C':count_the_number_of_vacancies('C'),
    #     'Shell':count_the_number_of_vacancies('Shell')
    # }
    # print(dictionary_of_vacancies)

    # get_salary_from_vacancies('https://api.hh.ru/vacancies?text=%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82%20Python')
    #
    # predict_rub_salary('Python')



    url = f'https://api.hh.ru/vacancies?text=%D0%9F%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%81%D1%82%20Python'
    response = requests.get(url)
    response.raise_for_status()

    for vacancy_index, vacancy_json in enumerate (response.json()['items']):
        pass
    print(vacancy_index)



