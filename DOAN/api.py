from flask import Flask, jsonify, render_template, request
import utils
import render_templates


app = Flask(__name__)

# define API
# get category in database
@app.route("/category", methods = ["GET"]) # define endpoint để thực thi API
def get_categories():
    rows = utils.get_all("SELECT  * FROM category")
    data = []
    for r in rows:
        data.append(
            { "id": r[0],
              "subject": r[1],
              "url": r[2]
            }
        )
    #return jsonify({"category": data})
    return render_template("category.html", data=data)

 # get tất cả news from database
@app.route("/news", methods = ["GET"]) # define endpoint để thực thi API
def get_news():
    kw = request.args.get("keywords", None)
    return render_template("news.html", data=render_templates.read_news(kw))
"""
    kw = request.args.get("keywords", None)
    if keywords:
        search_news_by_keywords(kw)
    else:
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
                "category_id": r[5],
                "category_name": r[6]
            })
    #return jsonify({"news": data})

"""
#get một news by id from database
@app.route("/news/<int:news_id>", methods = ["GET"])
def get_news_by_id(news_id):
    r = utils.get_news_id(news_id)
    data = {
        "id": r[0],
        "subject": r[1],
        "description": r[2],
        "image": r[3],
        "original_url": r[4],
        "category_name": r[5]
    }
    return jsonify({"news_found": data})

#find news dựa vào keyword
@app.route("/news/<keywords>", methods = ["GET"])
def get_news_by_keywords(keywords):
    rows = utils.get_news_by_kw(keywords)
    data = []
    for r in rows:
        data.append(
        {
            "id": r[0],
            "subject": r[1],
            "description": r[2],
            "image": r[3],
            "original_url": r[4],
            "category_id": r[5],
            "category_name": r[6]
        })
    return jsonify({"news_by_kw": data})

#render templates
@app.route("/")
def render():
    kw = request.args.get("keywords", None)
    return render_template("index.html", data=render_templates.read_news(kw))

#search by keywords
@app.route("/news/<keywords>", methods = ["GET"])
def search_by_keywords(keywords):
    kw = request.args.get("keywords", None)
    if keywords:
        search_news_by_keywords(kw)
    return {"search_by_keywords": search_news_by_keywords(kw)}

# run module
if __name__ == "__main__":
    app.run()
