# import thư viện:
from flask import Flask, jsonify
import newspaper
from newspaper import Article
import sqlite3

from  pyvi import ViTokenizer as tach_tu
from Stopword import *
def match_data(keyword_format): # hàm trả về kết quả các bài báo liên quan tới key word
    conn = sqlite3.connect("data/crawlingDB.db")
    query = """SELECT * FROM news where description like ? or subject like ?"""
    data = conn.execute(query, (keyword_format,keyword_format)).fetchall()
    conn.commit()
    return data


def creat_word_count_dict(data):
    # tạo thư viện chứa các từ
    words = ""
    for item in data:
        for i in item:
            words += i

    words = tach_tu.tokenize(words)
    #print("Nội dung sau khi word segmentation: ",str(words))
    words = words.split()
    words_dict = set(words)
    #print("Các từ trong nội dung: ",words_dict)
    words_count_dict = dict.fromkeys(words_dict, 0)

    # đếm số lượng từ xuất hiện trong thư viện
    for word in words:
        words_count_dict[word] += 1
    return dict(words_count_dict)

def compute_TF(word_count_dict, bow):
    tf_dict = {}
    bow_count = len(bow)
    for word, count in word_count_dict.items():
        tf_dict[word] = round(count/float(bow_count),2)
    #print("compute_TF", tf_dict) ###
    return tf_dict


def compute_IDF(doc_list):
    import math
    idf_dict = {}
    N = len(doc_list)

    idf_dict = dict.fromkeys(doc_list.keys(), 0)

    for word, count in doc_list.items():
        if count > 0:
            idf_dict[word] += 1

    for word, count in idf_dict.items():
        idf_dict[word] = round(math.log(N / float(count)),2)
    #print("compute_IDF", idf_dict)  ###
    return idf_dict

def compute_TFIDF(tf_bow, idfs):
    tfidf = {}
    for word, val in tf_bow.items():
        tfidf[word] = round((val*idfs[word]),2)
    #print("compute_TFIDF", tfidf)  ###
    return tfidf



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
def search_by_keywords_cuathay(keywords = None):
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










def get_news_by_kw(keywords = None):
    conn = sqlite3.connect("DATA/crawlingDB.db")
    data = []
    if keywords is not None:
        #news = get_all("SELECT * FROM news")
        keyword_format = "%{}%".format(keywords)
        keyword_tokennize = tach_tu.tokenize(keywords)
        print("Từ khoá: ", keyword_tokennize)

        # output
        bow = str(keyword_tokennize).split(' ')
        print("bow tìm kiếm :", bow)
        print("------------------------------------------------------------")

        # xử lí
        news_match = 1  # đánh dấu số lượng bài viết match với keyword
        list_news_match = []  # list chứa if_idf và link bài viết
        sort_new_by_tf_idf = []  # list chứa tf_idf của các bài viết match với keyword -> dùng để sắp xếp theo thứ tự
        for row in match_data(keyword_format):  # với mỗi bài báo liên quan tới keyword, tiến hành tính tf-idf
            data_match = loai_bo_stopword(str(row[2]))  # loại bỏ stopword
            word_dict = creat_word_count_dict(data_match)  # tạo bag of word đếm số lần xuất hiện
            # print("Số lần xuất hiện :",word_dict)
            # tính TF
            tf = compute_TF(word_dict, bow)
            # print("Kết quả tf:", tf)
            # Tính IDF
            idf = compute_IDF(word_dict)
            # print("Kết quả idf:", idf)
            # Cuối cùng: Tính TF-IDF Từ kết quả TF và IDF phía trên chỉ cần nhân lại là xong
            tf_idf = compute_TFIDF(tf, idf)
            #print(tf_idf)
            for key, value in tf_idf.items():  # tạo vòng lặp tìm ra keyword và tf_idf của nó,  -> tf_idf = value
                if (key == keyword_tokennize):
                    #print("****Bài số ", news_match)
                    news_match += 1  # tăng số lượng bài viết lên
                    #print("tf-idf(" + str(key) + "):", value)
                    #print("id :", row[0])
                    #print("Mô tả: ", row[1])
                    #print("Link:", row[2])

                    data.append(get_news_id(row[0]))

                    #new = {value: row[1]}
                    #list_news_match.append(new)  # chứa tf_idf của keyword và link bài viết chứa keyword
                    #sort_new_by_tf_idf.append(value)  # thêm tf_idf vào list

                    #print("--------------------------------------------------------------------------------")
        # sau khi lặp xong
        # -> sắp sếp giảm dần
        #  -> hiện kết quả tìm kiếm
        #sort_new_by_tf_idf.sort(reverse=True)
        #print(sort_new_by_tf_idf)
        #print(list_news_match)

        #print(data)
    conn.close()
    return data






if __name__ == "__main__":
    #print(get_news_id(13)[1])
    #print(get_news_url())
    print(get_news_by_kw("SUV"))