from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:hoangtuyen@12@localhost/database_QLSV?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)

if __name__ == '__main__':
    app.run(debug=True)