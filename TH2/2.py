chuoi = input('Nhập chuỗi cách nhau bởi dấu phẩy :')
list = chuoi.split(',')
list.sort()
for i in list:
    print(i)