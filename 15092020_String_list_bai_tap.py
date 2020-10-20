'''
#Bài 1
name = input("Nhap vao ho va ten: ")
print("Ten cua ban la: " + name[0:])
print("In nguoc ten cua ban: " + name[::-1])
print("-----------------------------------------")
#Bài 2
long = input("Nhập vào tên của Long :")
tuyen = input("Nhập vào tên của Tuyến :")
if len(long) < len(tuyen):
    print(tuyen +" là best ok!")
print("-----------------------------------------")

#Bài 3
chuoi = input("Nhập vào dãy số( cách nhau bởi dấu phẩy) :")
list = chuoi.split(',');
sum =0
for i in list:
    sum = sum + int(i)
print("Tổng s = ", sum)
print("-----------------------------------------")
'''
#Bài 4
my_str = input("Nhập vào chuỗi của bạn :")
print("Chuỗi của bạn sau khi in hoa: " + my_str.upper())