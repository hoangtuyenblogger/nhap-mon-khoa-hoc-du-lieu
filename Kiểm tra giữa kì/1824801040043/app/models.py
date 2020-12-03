from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db
from sqlalchemy import or_, and_


class KHACHHANG(db.Model):
    MAKH = Column(String(50), primary_key=True)
    TENKH = Column(String(256))
    DIACHI = Column(String(256))
    LOAIKH = Column(String(256))
    DIENTHOAIS = relationship("DIENTHOAI", backref="KHACHHANG", lazy=True)
    def __init__(self,MAKH,TENKH,DIACHI,LOAIKH):
        self.MAKH = MAKH
        self.TENKH = TENKH
        self.DIACHI = DIACHI
        self.LOAIKH = LOAIKH
def insert_into_KHACHHANG():
    row =KHACHHANG(MAKH = "1", TENKH = "Hoàng Tuyến", DIACHI = "Thủ Dầu Một", LOAIKH = "Cá nhân")
    row1 = KHACHHANG(MAKH="2", TENKH="Nguyễn Văn An", DIACHI="Bình Dương", LOAIKH="Doanh nghiệp")
    db.session.add(row)
    db.session.commit()
    db.session.add(row1)
    db.session.commit()
    print("2 row ADDED. . . ")
#####################################################################################
class DIENTHOAI(db.Model):
    SODT = Column(String(20), primary_key= True)
    MAKH = Column(String(50), ForeignKey(KHACHHANG.MAKH))# khoá ngoại
    LOAIDT = Column(String(50))  # vô tuyến, dây cáp
    SOHD = Column(String(50))
    DICHVUs = relationship("DICHVU", secondary= "dienthoai_dichvu")
    def __init__(self,SODT,MAKH,LOAIDT,SOHD):
        self.SODT = SODT
        self.MAKH = MAKH
        self.LOAIDT = LOAIDT
        self.SOHD = SOHD
def insert_into_DIENTHOAI():
    row = DIENTHOAI(SODT = "0347133942",MAKH = "1", LOAIDT = "Vô tuyến", SOHD="HD_1")
    row1 = DIENTHOAI(SODT = "01684659538",MAKH = "2", LOAIDT = "Dây cáp", SOHD="HD_2")
    db.session.add(row)
    db.session.commit()
    db.session.add(row1)
    db.session.commit()
    print("2 row ADDED. . . ")
#####################################################################################
class DICHVU(db.Model):
    MADV = Column(String(50), primary_key=True)
    TENDV = Column(String(256))
def insert_into_DICHVU():
    row = DICHVU(MADV="dv1", TENDV="SMS")
    row1 = DICHVU(MADV="dv2", TENDV="funring")
    db.session.add(row)
    db.session.commit()
    db.session.add(row1)
    db.session.commit()
    print("2 row ADDED. . . ")
#####################################################################################
class DANGKI(db.Model):
    __tablename__ = 'dienthoai_dichvu'
    MADV = Column(String(50), ForeignKey(DICHVU.MADV), primary_key=True)
    SODT = Column(String(20), ForeignKey(DIENTHOAI.SODT),  primary_key=True)
    DICHVUS = relationship("DICHVU",backref = "dangky_dichvu",lazy=True)
    DIENTHOAIS = relationship("DIENTHOAI",backref="dangky_dienthoai",lazy = True)
def insert_into_DANGKI():
    row = DANGKI(MADV="dv1", SODT = "0347133942")
    row1 = DANGKI(MADV="dv2", SODT="01684659538")
    db.session.add(row)
    db.session.commit()
    db.session.add(row1)
    db.session.commit()
    print("2 row ADDED. . . ")
#####################################################################################
def Creat_database():
    db.create_all()
#####################################################################################


def cau_a():
    r = DICHVU.query.join(DANGKI, DICHVU.MADV == DANGKI.MADV).join(DIENTHOAI, DANGKI.SODT == DIENTHOAI.SODT).join(
        KHACHHANG, DIENTHOAI.MAKH == KHACHHANG.MAKH).filter(KHACHHANG.LOAIKH == "Cá nhân").add_columns(KHACHHANG.TENKH,
                                                                                                       DICHVU.TENDV).all()
    print("Câu 2a, các dịch vụ cho khách hàng cá nhân: ")
    for i in r:
        print("Họ tên: " + i.TENKH + " \nDịch vụ: " + i.TENDV)
    print("-------------------------------------------------------")
def cau_b():
    r = DICHVU.query.join(DANGKI, DICHVU.MADV == DANGKI.MADV).join(DIENTHOAI, DANGKI.SODT == DIENTHOAI.SODT).join(
        KHACHHANG, DIENTHOAI.MAKH == KHACHHANG.MAKH).filter(DICHVU.TENDV == "SMS",
                                                            KHACHHANG.LOAIKH == "Cá nhân").add_columns(KHACHHANG.TENKH,
                                                                                                       DICHVU.TENDV).all()
    print("Câu 2b, các dịch vụ SMS cho khách hàng cá nhân")
    for i in r:
        print("Họ tên: " + i.TENKH + " \nDịch vụ: " + i.TENDV)
    print("-------------------------------------------------------")
def cau_c():
    r = DICHVU.query.join(DANGKI, DICHVU.MADV == DANGKI.MADV).join(DIENTHOAI, DANGKI.SODT == DIENTHOAI.SODT).join(
        KHACHHANG, DIENTHOAI.MAKH == KHACHHANG.MAKH).filter(DICHVU.TENDV == "SMS", or_(KHACHHANG.LOAIKH == "Cá nhân",
                                                                                       KHACHHANG.LOAIKH == "Doanh nghiệp", )).add_columns(
        KHACHHANG.TENKH, DICHVU.TENDV).all()
    print("Câu 2c, các dịch vụ cho cá nhân hoặc doanh nghiệp")
    for i in r:
        print("Họ tên: " + i.TENKH + " \n Dịch vụ: " + i.TENDV)
    print("-------------------------------------------------------")
def cau_d():
    r = DICHVU.query.join(DANGKI, DICHVU.MADV == DANGKI.MADV).join(DIENTHOAI, DANGKI.SODT == DIENTHOAI.SODT).join(
        KHACHHANG, DIENTHOAI.MAKH == KHACHHANG.MAKH).filter(
        or_(KHACHHANG.TENKH.contains("%Anh"), KHACHHANG.TENKH.contains("%An"))).add_columns(KHACHHANG.TENKH,
                                                                                            DICHVU.TENDV).all()
    print("Câu 2d, Các dịch vụ có khách hàng tên Anh hoặc An:")
    for i in r:
        print("Họ tên: " + i.TENKH + " \n Dịch vụ: " + i.TENDV)
    print("-------------------------------------------------------")

def cau_e():
    r = DICHVU.query.join(DANGKI, DICHVU.MADV == DANGKI.MADV).join(DIENTHOAI, DANGKI.SODT == DIENTHOAI.SODT).join(
        KHACHHANG, DIENTHOAI.MAKH == KHACHHANG.MAKH).filter(KHACHHANG.TENKH.contains("Nguyễn%")).add_columns(
        KHACHHANG.TENKH, DICHVU.TENDV).all()
    print("Câu 2e,Các dịch vụ khách hàng họ Nguyễn đăng kí:")
    for i in r:
        print("Họ tên: " + i.TENKH + " \n Dịch vụ: " + i.TENDV)
    print("-------------------------------------------------------")


def cau_f():
    r = DICHVU.query.join(DANGKI, DICHVU.MADV == DANGKI.MADV).join(DIENTHOAI, DANGKI.SODT == DIENTHOAI.SODT).join(
        KHACHHANG, DIENTHOAI.MAKH == KHACHHANG.MAKH).filter(KHACHHANG.LOAIKH == "Doanh nghiệp",
                                                            KHACHHANG.DIACHI == "Bình Dương").add_columns(
        KHACHHANG.TENKH, DICHVU.TENDV, KHACHHANG.LOAIKH, KHACHHANG.DIACHI).all()
    print("Câu 2f, các dịch vụ doanh nghiệp Bình Dương đăng kí:")
    for i in r:
        print(
            "Họ tên: " + i.TENKH + " - Loại khách hàng: " + i.LOAIKH + " - Địa chỉ: " + i.DIACHI + " - Dịch vụ: " + i.TENDV)
    print("-------------------------------------------------------")

def cau_2():
    cau_a()
    cau_b()
    cau_c()
    cau_d()
    cau_e()
    cau_f()
if __name__ == '__main__':
    #Creat_database()
    #insert_into_KHACHHANG()
    #insert_into_DIENTHOAI()
    #insert_into_DICHVU()
    #insert_into_DANGKI()
    cau_2()

