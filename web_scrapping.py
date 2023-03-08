import requests
from bs4 import BeautifulSoup
 url = 'dailytrust.com/last-saturday-polls-raised-issues-that-require-immediate-solution-inec/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
print(soup.title.get_text())

paragraphs = soup.find_all('p')
for paragraph in paragraphs:
    print(paragraph.get_text())
