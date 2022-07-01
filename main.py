import requests
from bs4 import BeautifulSoup


person_url_list = []

for i in range(0, 740, 20):
  url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'
  
  q = requests.get(url)
  result = q.content

  soup = BeautifulSoup(result, 'lxml')
  persons = soup.find_all(class_='bt-open-in-overlay')

  for person in persons:
    person_page_url = person.get('href')
    person_url_list.append(person_page_url)
    
with open('persona_url_list.txt', 'a') as file:
  for line in person_url_list:
    file.write(f'{line}\n')
