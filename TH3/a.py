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
def test_crawler(url):
    #print("url nè hjhj", article.url)
    try:
        article = Article(url)
        article.download()
        article.parse()

        print("article.title: ",article.title)
        print("article.text: ",article.text)
        print("article.additional_data: ", article.additional_data)
        print("article.authors: ", article.authors)
        print("article.doc: ", article.doc)
        print("article.clean_doc: ", article.clean_doc)
        print("article.clean_top_node: ", article.clean_top_node)
        print("article.publish_date: ", article.publish_date)
        print("article.summary: ", article.summary)
        print("article.tags: ", article.tags)
        print("article.extractor: ", article.extractor)
    except Exception as ex:
        print("Erro: ", ex)
        pass


if __name__ == '__main__':
    print('helo')