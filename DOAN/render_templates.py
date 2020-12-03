import utils
import json

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


def get_news_id(news_id):
    news = []
    conn = sqlite3.connect("DATA/crawlingDB.db")
    query = """
    SELECT N.id, N.subject, N.description, N.image, N.original_url, C.name, C.url
    FROM news N INNER JOIN category C on N.category_id = C.id
    WHERE N.id=?
    """
    row = conn.execute(query,(news_id, )).fetchone()
    print(row)
    conn.close()
    new = [{'id': int(row[0])}, {'subject': row[1]}, {'description': row[2]}, {'image': row[3]},
               {'original_url': row[4]}, {'category_id': row[5]}]
    return new


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


#read category
def read_category():
    rows = utils.get_all("SELECT  * FROM category")
    data = []
    for r in rows:
        data.append(
            {"id": r[0],
             "subject": r[1],
             "url": r[2]
             }
        )
    with open("json_file/category.json", "w") as cat:
        json.dump(data, cat)
    #return render_template("category.html", data=data)

# read news
def get_news():
    rows = utils.get_all("SELECT * FROM news")
    data = []
    for r in rows:
        data.append(
        {
            "id": r[0],
            "subject": r[1],
            "description": r[2],
            "image": r[3],
            "original_url": r[4],
            "category_id": r[5]
        })
    with open("json_file/news.json", "w", encoding= "utf8") as f:
        json.dump(data, f)


def read_news(keywords = None):
    with open("json_file/news.json", encoding= "utf8") as f:
        news = json.load(f)
        print(news)
    if keywords:
        news = [n for n in news if n["subject"].lower().find(keywords.lower()) >= 0]
    return news



def read_news_cua_tuyen(keywords = None):

    conn = sqlite3.connect("DATA/crawlingDB.db")
    data = []
    if keywords is not None:
        # news = get_all("SELECT * FROM news")
        keyword_format = "%{}%".format(keywords)
        keyword_tokennize = tach_tu.tokenize(keywords)
        print("Từ khoá: ", keyword_tokennize)

        # output
        bow = str(keyword_tokennize).split(' ')
        print("bow tìm kiếm :", bow)
        print("------------------------------------------------------------")

        # xử lí
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
            # print(tf_idf)
            for key, value in tf_idf.items():  # tạo vòng lặp tìm ra keyword và tf_idf của nó,  -> tf_idf = value
                if (key == keyword_tokennize):
                    data.append(get_news_id(row[0]))

    conn.close()
    return data


if __name__ == "__main__":
    #read_category()
    #get_news()
   print(read_news_cua_tuyen("Thuỷ Tiên"))


