from flask import Flask, jsonify
import utils


app = Flask(__name__)
# 1. get category đưa lên website
@app.route("/category") #define endpoint để thực thi API
def get_category():
    rows = utils.get_all("SELECT * FROM category")
    data = []
    for r in rows:
        data.append(
            {
            "id":r[0],
            "subject": r[1],
            "url": r[2]
            }
        )
    return jsonify({"category":data})

# 2. API get news from database
@app.route("/news", methods = ["GET"]) # define endpoint để thực thi API
def get_news():
    rows = utils.get_all("SELECT * FROM news")
    data = []
    for r in rows:
        data.append(
            {
                "id":r[0],
                "subject": r[1],
                "description": r[2],
                "image": r[3],
                "original_url": r[4]
            }
        )

    return jsonify({"news": data})



# 3. API get một news by id from database
@app.route("/news/<int:news_id>", methods = ["GET"])
def get_news_id(news_id):
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

if __name__ == "__main__":
    app.run()