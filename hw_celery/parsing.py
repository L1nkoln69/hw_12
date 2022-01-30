# from bs4 import BeautifulSoup
# import requests
# # #
# page_number = 10
# for _ in range(10):
#     site = requests.get(f'https://quotes.toscrape.com/page/{page_number}').text
#     site = BeautifulSoup(site, 'lxml')
#     a = -1
#     author_info = site.find_all('div', {'class': 'quote'})
#     for author_one in author_info:
#         a += 1
#         quotes = site.find('div', {'class': 'container'}).find_all('span', {'class': 'text'})
#         authors = site.find('div', {'class': 'container'}).find_all('small', {'class': 'author'})
#
#         author_href = author_one.find('a').get('href')
#         new_request = requests.get(f'https://quotes.toscrape.com{author_href}').text
#         soup = BeautifulSoup(new_request, 'lxml')
#
#         abouts = soup.find('div', class_='author-description').text
#         born_date = soup.find('span', class_='author-born-date').text
#         born_location = soup.find('span', class_='author-born-location').text
#
#         author_s = Author.objects.filter(name=authors[a].text)
#         if not author_s:
#             Author.objects.create(name=authors[a].text, date_birthday=f'{born_date}, {born_location}', about=abouts)
#             Quotes.objects.create(quotes=quotes[a].text, author=Author.objects.last())
#         else:
#             Quotes.objects.create(quotes=quotes[a].text, author=author_s[0])
#     page_number += 1
# for _ in range(10):
#     site = requests.get(f'https://quotes.toscrape.com/page/{page_number}').text
#     site = BeautifulSoup(site, 'lxml')
#     a = -1
#     author_info = len(site.find_all('div', {'class': 'quote'}))
#     for author_one in range(author_info):
#         a += 1
#         quotes = site.find('div', {'class': 'container'}).find_all('span', {'class': 'text'})
#         authors = site.find('div', {'class': 'container'}).find_all('small', {'class': 'author'})
#
#         author_href = site.find_all('div', {'class': 'quote'})[a].find('a').get('href')
#         new_request = requests.get(f'https://quotes.toscrape.com{author_href}').text
#         soup = BeautifulSoup(new_request, 'lxml')
#
#         abouts = soup.find('div', class_='author-description').text
#         born_date = soup.find('span', class_='author-born-date').text
#         born_location = soup.find('span', class_='author-born-location').text
#
#         # db_authors = Author.objects.all()
#         # db_quotes = Quotes.objects.all()
#         print(quotes[a].text)
#     page_number += 1
