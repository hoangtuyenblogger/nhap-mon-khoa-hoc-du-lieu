url = 'http://www.phimmoizz.net/phim-le/'
import requests
from bs4 import BeautifulSoup

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

titles = soup.findAll('div', class_='movie-meta')
print(titles)

links = [link.find('a').atstr["href"] for link in titles]
print(links)