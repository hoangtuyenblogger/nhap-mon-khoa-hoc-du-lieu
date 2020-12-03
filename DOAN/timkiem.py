import sqlite3
import pandas as pd
from  pyvi import ViTokenizer as tach_tu
from Stopword import *
def match_data(keyword_format): # hàm trả về kết quả các bài báo liên quan tới key word
    conn = sqlite3.connect("data/crawlingDB.db")
    query = """SELECT subject, original_url,description FROM news where description like ? or subject like ?"""
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


def main():
    # input
    keyword = input("Nhập từ khoá tìm kiếm: ")
    keyword_format = "%{}%".format(keyword)
    keyword_tokennize = tach_tu.tokenize(keyword)
    print("Từ khoá: ",keyword_tokennize)

    # output
    bow = str(keyword_tokennize).split(' ')
    print("bow tìm kiếm :",bow)
    print("------------------------------------------------------------")


    # xử lí
    news_match = 1 # đánh dấu số lượng bài viết match với keyword
    list_news_match = [] # list chứa if_idf và link bài viết
    sort_new_by_tf_idf = [] # list chứa tf_idf của các bài viết match với keyword -> dùng để sắp xếp theo thứ tự
    for row in match_data(keyword_format): # với mỗi bài báo liên quan tới keyword, tiến hành tính tf-idf
        data = loai_bo_stopword(str(row[2])) # loại bỏ stopword
        word_dict = creat_word_count_dict(data) # tạo bag of word đếm số lần xuất hiện
        # print("Số lần xuất hiện :",word_dict)
        # tính TF
        tf = compute_TF(word_dict, bow)
        # print("Kết quả tf:", tf)
        # Tính IDF
        idf = compute_IDF(word_dict)
        # print("Kết quả idf:", idf)
        # Cuối cùng: Tính TF-IDF Từ kết quả TF và IDF phía trên chỉ cần nhân lại là xong
        tf_idf = compute_TFIDF(tf, idf)
        for key, value in tf_idf.items(): # tạo vòng lặp tìm ra keyword và tf_idf của nó,  -> tf_idf = value
            if (key == keyword_tokennize):
                print("****Bài số ",news_match)
                news_match +=1 # tăng số lượng bài viết lên
                print("tf-idf(" + str(key) + "):", value)
                print("Mô tả: ",row[0])
                print("Link:", row[1])
                new = {value:row[1]}
                list_news_match.append(new) # chứa tf_idf của keyword và link bài viết chứa keyword
                sort_new_by_tf_idf.append(value) # thêm tf_idf vào list

                print("--------------------------------------------------------------------------------")
    # sau khi lặp xong
    # -> sắp sếp giảm dần
    #  -> hiện kết quả tìm kiếm
    sort_new_by_tf_idf.sort(reverse=True)
    print(sort_new_by_tf_idf)
    print(list_news_match)



if __name__ == '__main__':
    while True:
        main()
    '''a = "Thụy Điển tăng thuế bia rượu để thêm tiền chi cho quốc phòng"
    print(a)
    print(tach_tu.tokenize(a))'''