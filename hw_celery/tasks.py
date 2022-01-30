from hw_12.celery import app
from django.core.mail import send_mail
from bs4 import BeautifulSoup
import requests
from .models import Author, Quotes
from celery import shared_task


@app.task
def my_send_mail(email, remind):
    send_mail('REMINDER',
              f'{remind}',
              'orlov229003@gmail.com',
              [email],
              fail_silently=False
              )


@app.task
def to_me_send_mail(pages):
    send_mail('Parsing',
              f'цитат больше нету на странице ({pages})',
              'orlov229003@gmail.com',
              ['orlav228007@gmail.com'],
              fail_silently=False
              )


@shared_task
def parsing_site():
    page_number = 1
    site = requests.get(f'https://quotes.toscrape.com/page/{page_number}').text
    site = BeautifulSoup(site, 'lxml')
    author_info = len(site.find_all('div', {'class': 'quote'}))
    a = -1
    for author_one in range(author_info + 1):
        counter = 0
        id_objects = 0
        if counter == 5:
            break
        else:
            a += 1
            id_objects += 1
            quotes = site.find('div', {'class': 'container'}).find_all('span', {'class': 'text'})
            authors = site.find('div', {'class': 'container'}).find_all('small', {'class': 'author'})

            db_authors = Author.objects.all()
            db_quotes = Quotes.objects.all()
            try:
                author_href = site.find_all('div', {'class': 'quote'})[a].find('a').get('href')
                new_request = requests.get(f'https://quotes.toscrape.com{author_href}').text
                soup = BeautifulSoup(new_request, 'lxml')

                abouts = soup.find('div', class_='author-description').text
                born_date = soup.find('span', class_='author-born-date').text
                born_location = soup.find('span', class_='author-born-location').text
                id_author = Author.objects.filter(name=authors[a].text)
                if authors[a].text in db_authors:
                    if quotes[a].text in db_quotes:
                        continue
                    else:
                        Quotes.objects.create(quotes=quotes[a].text, authors_id=id_author[id_objects].id)
                        counter += 1
                else:
                    Author.objects.create(name=authors[a].text,
                                          date_birthday=f'{born_date}, {born_location}',
                                          about=abouts)
                    Quotes.objects.create(quotes=quotes[a].text, authors_id=id_author[id_objects].id)
                    counter += 1
            except IndexError:
                to_me_send_mail(page_number)
                page_number += 1
