from datetime import date
from flask import Flask, jsonify
import newspaper
from newspaper import Article
import sqlite3

#define function get category, hoặc get news from database
#tạo conn để connect tới DB,
#thực thi query để lấy dữ liệu từ DB,
#đóng conn.
# fetchall để lấy tất cả dữ liệu
def get_all(query):
    conn = sqlite3.connect("DATA/crawlingDB") # create connection
    data = conn.execute(query).fetchall()  # get all data
    conn.close()
    return data

    # define function get news from database by id of news
    # lấy 1 tin nên dùng fetchone(), truyền news_id ở dạng tuple



    #define function Add bài báo được craw từ web vào database, sử dụng newspaper3k
    # #tạo query để insert bài báo craw được vào table news,
    # gọi conn.commit() để add vào database
    # url: tuoitre.vn/bai-bao-thu-nhat, category_id = 1
def add_news(conn,url,category_id):
    query = """
            INSERT INTO news(subject, desciption,image,original_url,category_id) values(?,?,?,?,?)
            """
    article = Article(url)
    article.download()
    article.parse()

    conn.execute(query, (article.title, article.text, article.top_image, article.url, category_id)) # ex, add row to talbe
    conn.commit()

# get news from root url, import to database
def get_news_url():
    cats = get_all("SELECT * FROM category")
    conn = sqlite3.connect("DATA/crawlingDB")

    for cat in cats:
        cat_id = cat[0]
        url = cat[2]
        cat_paper = newspaper.build(url)
        for article in cat_paper.articles:
            try:
                print("url nè hjhj", article.url)
                add_news(conn,article.url,cat_id) # import to database
            except Exception as ex:
                print("Erro: ", ex)
                pass
        conn.close()

def get_news_id(news_id):
    conn = sqlite3.connect("DATA/crawlingDB")
    query = """
    SELECT N.id, N.subject, N.description, N.image, N.original_url, C.name, C.url
    FROM news N INNER JOIN category C on N.category_id = C.id    WHERE N.id=?
    """
    news = conn.execute(query, (news_id,)).fetchone()
    conn.close()
    return news

if __name__ == '__main__':
    print("helo")
    #get_news_url()