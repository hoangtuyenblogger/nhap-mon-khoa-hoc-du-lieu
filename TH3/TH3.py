def helo(name, class_name="D18HT01", *args):
    print(f"helo {name} học lớp {class_name}")
    for arg in args:
        print(arg)

def helo2(name, class_name="D18HT01", **kwargs):
    print(f"helo {name} học lớp {class_name}")
    for key,value in kwargs:
        print(key,value)


def demo():
    my_list = ["NHập môn khdl","sáng thứ 3"]
    print(type(my_list))
    helo("tuyến", "d18ht02", "NHập môn khdl","sáng thứ 3")

    print("----------------------------------------------------------")
    helo2("tuyến", "d18ht01", tiet=5,thu=3)


dict2 = {1:{1: 'Quantrimang.com','name': 'Công nghệ'}}

row = dict2[1]
print(type(row))
for i in row:
    print(i)