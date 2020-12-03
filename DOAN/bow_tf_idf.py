import sqlite3
import pandas as pd
from  pyvi import ViTokenizer as tach_tu
def creat_word_count_dict(keyword):
    conn = sqlite3.connect("data/crawlingDB.db")
    query = """SELECT description FROM news where description like ?"""
    a = conn.execute(query,(keyword,)).fetchall()
    conn.commit()


    # tạo thư viện chứa các từ
    words = ""
    for item in a:
        for i in item:
            words += i

    words = tach_tu.tokenize(words)
    #print(words)
    words = words.split()
    words_dict = set(words)
    #print("Các từ trong nội dung: ",words_dict)
    words_count_dict = dict.fromkeys(words_dict, 0)

    # đếm số lượng từ xuất hiện trong thư viện
    for word in words:
        words_count_dict[word] += 1
    conn.close()
    return dict(words_count_dict)

def compute_TF(word_count_dict, bow):
    tf_dict = {}
    bow_count = len(bow)
    for word, count in word_count_dict.items():
        tf_dict[word] = round(count/float(bow_count),2)

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

    return idf_dict

def compute_TFIDF(tf_bow, idfs):
    tfidf = {}
    for word, val in tf_bow.items():
        tfidf[word] = round((val*idfs[word]),2)
    return tfidf


def main():
    keyword = input("Nhập từ khoá tìm kiếm: ")
    keyword_format = "%{}%".format(keyword)
    keyword_tokennize = tach_tu.tokenize(keyword)
    print("Từ khoá: ",keyword_tokennize)

    bow = str(keyword_tokennize).split(' ')
    print("bow tìm kiếm :",bow)
    word_dict = creat_word_count_dict(keyword_format)
    print("Số lần xuất hiện :",word_dict)
    # tính TF
    tf = compute_TF(word_dict, bow)
    print("Kết quả tf:", tf)
    # Tính IDF
    idf = compute_IDF(word_dict)
    print("Kết quả idf:", idf)
    # Cuối cùng: Tính TF-IDF Từ kết quả TF và IDF phía trên chỉ cần nhân lại là xong
    tf_idf = compute_TFIDF(tf, idf)
    for key, value in tf_idf.items():
        if( key == keyword_tokennize):
            print(key,":", value)
    #print(sorted(tf_idf.values(),reverse=True))
    print(tf_idf)

    # vẽ biểu đồ
    df = pd.DataFrame([tf_idf])
    #df.plot
if __name__ == '__main__':
    main()
