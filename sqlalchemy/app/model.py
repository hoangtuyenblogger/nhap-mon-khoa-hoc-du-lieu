from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Khoa(db.Model):
    makhoa = Column(String(10), primary_key=True)
    tenkhoa = Column(String(50), nullable=False)
    lops = relationship("Lop", backref="Khoa", lazy=True)

class Lop(db.Model):
    malop = Column(String(10), primary_key=True)
    tenlop = Column(String(50), nullable=False)
    nienkhoa = Column(String(100), nullable= False)
    makhoa = Column(String(10), ForeignKey(Khoa.makhoa))
    sinhviens = relationship("Sinhvien", backref="Lop", lazy=True)

class Sinhvien(db.Model):
    masv = Column(String(14), primary_key= True)
    hosv = Column(String(25), nullable= False)
    tenlotsv = Column(String(50), nullable= True)
    tensv = Column(String(50), nullable= False)
    ngaysinh = Column(String(40))
    noisinh = Column(String(250))
    malop = Column(String(10), ForeignKey(Lop.malop))


class Monhoc(db.Model):
    mamh = Column(String(10), primary_key=True, nullable=False)
    tenmh = Column(String(30), nullable=False)
    sotc = Column(String(10), nullable=True)
    makhoa_mh = Column(String(10), ForeignKey(Khoa.makhoa))
    sinhviens = relationship('Sinhvien', secondary='diemso')

class Diemso(db.Model):
    mamh = Column(String(10), ForeignKey(Monhoc.mamh),primary_key=True, nullable=False)
    masv = Column(String(15), ForeignKey(Sinhvien.masv), primary_key=True, nullable=False)
    diem = Column(String(5))
    sinhviens = relationship('Sinhvien', backref='diemso_sinhvien')
    monhocs = relationship('Monhoc', backref='diemso_monhoc')

def creat_database():
    db.create_all()
def insert_KHOA(_makhoa, _tenkhoa):
    try:
        row = Khoa(makhoa=_makhoa, tenkhoa=_tenkhoa)
        db.session.add(row)
        db.session.commit()
        print("Added KHOA(",_makhoa,",",_tenkhoa,")")
    except Exception as erro:
        print(erro)
if __name__ == '__main__':
    '''makhoa = input("Nhập mã khoa:").title()
    tenkhoa = input("Nhập tên khoa:").title()
    insert_KHOA(makhoa,tenkhoa)'''


