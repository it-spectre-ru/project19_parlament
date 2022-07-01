import requests
from bs4 import BeautifulSoup

for i in range(0, 740, 20):
  url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=20&noFilterSet=true&offset={i}'
  print(url)