from hw_12.celery import app
from django.core.mail import send_mail
from bs4 import BeautifulSoup
import requests
from models import Author, Quotes


@app.task
def my_send_mail(email, remind):
    send_mail('REMINDER',
              f'{remind}',
              'orlov229003@gmail.com',
              [email],
              fail_silently=False
              )


@app.task
def to_me_send_mail(email, remind):
    send_mail('Parsing',
              'цитат больше нету',
              'orlov229003@gmail.com',
              ['orlav228007@gmail.com'],
              fail_silently=False
              )


@app.task
def parsing_site():
    page_number = 1
    for _ in range(10):
        site = requests.get(f'https://quotes.toscrape.com/page/{page_number}').text
        site = BeautifulSoup(site, 'lxml')
        a = -1
        author_info = site.find_all('div', {'class': 'quote'})
        for author_one in author_info:
            a += 1
            quotes = site.find('div', {'class': 'container'}).find_all('span', {'class': 'text'})
            authors = site.find('div', {'class': 'container'}).find_all('small', {'class': 'author'})

            author_href = author_one.find('a').get('href')
            new_request = requests.get(f'https://quotes.toscrape.com{author_href}').text
            soup = BeautifulSoup(new_request, 'lxml')

            abouts = soup.find('div', class_='author-description').text
            born_date = soup.find('span', class_='author-born-date').text
            born_location = soup.find('span', class_='author-born-location').text

            author_s = Author.objects.filter(name=authors[a].text)
            if not author_s:
                Author.objects.create(name=authors[a].text, date_birthday=f'{born_date}, {born_location}', about=abouts)
                Quotes.objects.create(quotes=quotes[a].text, author=Author.objects.last())
            else:
                Quotes.objects.create(quotes=quotes[a].text, author=author_s[0])
        page_number += 1
