from app import db
from sqlalchemy import or_, and_
from app.model import *


if __name__ == '__main__':
    k1 = Khoa.query.filter(Khoa.tenkhoa.startswith('C')).all()
    print(k1)