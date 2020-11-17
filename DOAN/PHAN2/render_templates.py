import utils
import json

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
    if keywords:
        news = [n for n in news if n["subject"].lower().find(keywords.lower()) >= 0]
    return news

if __name__ == "__main__":
    #read_category()
    #get_news()
   print(read_news("suv"))