from bs4 import BeautifulSoup
import requests
import csv

respose = requests.get('https://coreyms.com/')

soup = BeautifulSoup(respose.content,"html.parser")

news = soup.findAll('article')


# find all title
titles = [i.find('a').text for i in news]
print("All title : ",titles)

#find all link news
link_news = [i.find('a').attrs["href"] for i in news]
print("All link news : ",link_news)


#find all short content
short_contents = [i.find('div', class_="entry-content") for i in news]
content = [i.find('p').text for i in short_contents]
print("ALl short content : ",content)

#find all links youtube videos
links_youtube_video = [i.find('a').attrs["href"] for i in news]
print("ALl links youtube video : ", links_youtube_video)



# save data to file csv
f = open("coreyms.csv", "w") # mở file ở chế độ cho phép ghi
f_writer = csv.writer(f)
f_writer.writerows(["Title","Link new","Short content","Link video"])


# print all news
for i in range(0,len(news),1):
    print("Title: ",titles[i])
    print("Link news: ",link_news[i])
    print("Short content: ",content[i])
    print("Link video: ", links_youtube_video[i])
    print("----------------------------------------------------------------------------------")
    #f_writer.writerow([titles[i],link_news[i],content[i],links_youtube_video[i]])
