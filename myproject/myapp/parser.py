import requests
from bs4 import BeautifulSoup
from .models import Vacancy

def parse_hh(query):
    url = f'https://hh.ru/search/vacancy?text={query}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    vacancies = soup.find_all('div', class_='vacancy-serp-item')

    for vacancy in vacancies:
        title = vacancy.find('a', class_='bloko-link').text
        company = vacancy.find('div', class_='vacancy-serp-item__meta-info-company').text
        location = vacancy.find('span', class_='vacancy-serp-item__meta-info').text
        description = vacancy.find('div', class_='vacancy-serp-item__snippet').text
        url = vacancy.find('a', class_='bloko-link')['href']

        Vacancy.objects.create(
            title=title,
            company=company,
            location=location,
            description=description,
            url=url
        )