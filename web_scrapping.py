import requests
from bs4 import BeautifulSoup
 
url = 'https://dailytrust.com/last-saturday-polls-raised-issues-that-require-immediate-solutions-inec/'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

print(soup.get_text('article', {'class':"body article__body"}))

paragraphs = soup.find_all('p')

print(soup.title)

for paragraph in paragraphs:
    if not paragraph.find_all('a'):
        print(paragraph.get_tech())