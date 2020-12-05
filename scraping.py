# Script for webpage scraping 

import requests
from bs4 import BeautifulSoup

url = 'https://www.cyberpunk.net/gb/en/pre-order?gclid=EAIaIQobChMI5q64hcG07QIVyLHtCh1rhg3iEAAYASAAEgIXU_D_BwE'

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title)
print(soup.p.text)

