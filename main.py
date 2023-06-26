import requests
from bs4 import BeautifulSoup

target_url = ""

response = requests.get(target_url)

soup = BeautifulSoup(response.text)

for link in soup.find_all('a'):
    print(link.get('href'))
