import requests
from bs4 import BeautifulSoup

response = requests.get("https://tuoitre.vn/tin-moi-nhat.htm")
soup = BeautifulSoup(response.content, "html.parser")

titles = soup.findAll('h3', class_='title-news')

links = [link.find('a').attrs["href"] for link in titles]
print(links)

for link in links:
    news = requests.get("https://tuoitre.vn" + link)
    soup = BeautifulSoup(news.content, "html.parser")
    title = soup.find("h1", class_="article-title").text
    abstract = soup.find("h2", class_="sapo").text
    body = soup.find("div", id="main-detail-body")
    content = body.findChildren("p", recursive=False)[0].text + body.findChildren("p", recursive=False)[1].text
    image = body.find("img").attrs["src"]
    print("Tiêu đề: " + title)
    print("Mô tả: " + abstract)
    print("Nội dung: " + content)
    print("Ảnh minh họa: " + image)