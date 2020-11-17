# import thư viện:
from flask import Flask, jsonify
import newspaper
from newspaper import Article
import sqlite3

#define function get all from database
#docstr: tạo conn để connect tới DB, thực thi query để lấy dữ liệu từ DB, đóng conn.
# \fetchall để lấy tất cả dữ liệu

def get_all(query):
    conn = sqlite3.connect("DATA/crawlingDB.db")
    data = conn.execute(query).fetchall()
    conn.close()

    return data

# define function get news from database by id of news
# lấy 1 tin nên dùng fetchone(), truyền news_id ở dạng tuple
def get_news_id(news_id):
    conn = sqlite3.connect("DATA/crawlingDB.db")
    query = """
    SELECT N.id, N.subject, N.description, N.image, N.original_url, C.name, C.url
    FROM news N INNER JOIN category C on N.category_id = C.id
    WHERE N.id=?
    """
    news = conn.execute(query,(news_id, )).fetchone()
    conn.close()
    return news


#define functin Add bài báo được crawling từ web vào server sử dụng newspaper3k
#tạo query để insert bài báo craw được vào table news, gọi conn.commit() để add vào database
def add_news(conn,url,category_id):
    query = """
    INSERT INTO news(subject,description,image,original_url,category_id)
    VALUES(?,?,?,?,?)
    """
    article = Article(url)
    article.download()
    article.parse()

    conn.execute(query, (article.title,article.text,article.top_image,article.url,category_id))
    conn.commit()



# API lấy danh mục bài báo sử dụng newspaper3k
#cats: gọi function get_all để lấy tất cả danh mục web có trong category
# tạo connection tới database
# với mỗi category được lấy, sẽ tiến hành lấy id, url, sau đó gọi method build của newspaper\
# để build link.
# với mỗi link sẽ gọi function add_news để add nội dung bài báo craw được vào database,
# sử dụng try - except để bỏ qua một số trường hợp không thể parse.
def get_news_url():
    cats = get_all("SELECT * FROM category") # lấy danh mục web từ DB
    conn = sqlite3.connect("DATA/crawlingDB.db") # tạo connect tới DB
    for cat in cats: # với mỗi trang trong DB
        cat_id = cat[0] # lấy id
        url = cat[2] # lấy link gốc
        cat_paper = newspaper.build(url) # dùng phương thức build của newspaper tạo ra các link cần craw
        for article in cat_paper.articles:
            try:
                print("===",article.url)
                add_news(conn,article.url,cat_id)# gọi add_news để add link dl vào DB
            except Exception as ex:
                print("ERROR:" + str(ex))
                pass

    conn.close() # đóng kết nối

# define function get news from database by str of news
# lấy 1 tin nên dùng fetchone(), truyền news_str ở dạng tuple
def get_news_by_kw(keywords = None):
    conn = sqlite3.connect("DATA/crawlingDB.db")
    if keywords is not None:
        #news = get_all("SELECT * FROM news")
        news_by_kw = [n for n in get_all("SELECT N.*, C.name FROM news N,category C where N.category_id = C.id") if n[1].lower().find(keywords.lower()) >= 0]
        data =[]
        for n in news_by_kw:
            data.append(get_news_id(n[0]))
        #print(data)
    conn.close()
    return data

#define function search theo keyword truyền vào form
def search_by_keywords(keywords = None):
    conn = sqlite3.connect("DATA/crawlingDB.db")
    if keywords is not None:
        # news = get_all("SELECT * FROM news")
        search_news_by_kw = [n for n in get_all("SELECT * FROM news") if n[1].lower().find(keywords.lower()) >= 0]
        data = []
        for n in search_news_by_kw:
            data.append(get_news_id(n[0]))
        # print(data)
    conn.close()
    return data

if __name__ == "__main__":
    #print(get_news_id(13)[1])
    #print(get_news_url())
    print(get_news_by_kw("iphone"))