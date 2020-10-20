'''4.	Viết chương trình nhập vào hai chuỗi, in ra chuỗi có chiều dài lớn hơn,
nếu hai chuỗi có độ dài bằng nhau thì in ra cả hai.4.	Viết chương trình nhập vào hai chuỗi,
in ra chuỗi có chiều dài lớn hơn, nếu hai chuỗi có độ dài bằng nhau thì in ra cả hai.'''

str1 = input('Nhập chuỗi thứ nhất :')
str2 = input('Nhập chuỗi thứ hai :')
if(len(str1) > len(str2)):
    print(str1)
elif(len(str1) < len(str2)):
    print(str2)
else:
    print(str1 + '\n' + str2)