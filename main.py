from unittest import result
import requests
from bs4 import BeautifulSoup


# person_url_list = []

# for i in range(0, 740, 20):
#   url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'
  
#   q = requests.get(url)
#   result = q.content

#   soup = BeautifulSoup(result, 'lxml')
#   persons = soup.find_all(class_='bt-open-in-overlay')

#   for person in persons:
#     person_page_url = person.get('href')
#     person_url_list.append(person_page_url)
    
# with open('persona_url_list.txt', 'a') as file:
#   for line in person_url_list:
#     file.write(f'{line}\n')


# with open('persona_url_list.txt') as file:

#   lines = [line.strip() for line in file.readlines()]

#   for line in lines:
#     q = requests.get(line)
#     result = q.content

#     soup = BeautifulSoup(result, 'lxml')
#     person = soup.find(class_='bt-biografie-name').find('h3').text
#     person_name_company = person.strip().split(',')
#     person_name = person_name_company[0]
#     person_company = person_name_company[1]



q = requests.get('https://www.bundestag.de/en/members/zimmermann_jens-858214')
result = q.content

soup = BeautifulSoup(result, 'lxml')
person = soup.find(class_='bt-biografie-name').find('h3').text
person_name_company = person.strip().split(',')
person_name = person_name_company[0]
person_company = person_name_company[1]

print(person_name)
print(person_company)

