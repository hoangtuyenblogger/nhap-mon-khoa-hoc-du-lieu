def chuoithuannghich(s):
    str1 = s
    str2 = s[::-1] # dao nguoc chuoi
    if(str1 == str2):
        return True
    return False

my_string = input('Nhập vào chuỗi : ')
if(chuoithuannghich(my_string)):
    print('Đây là chuỗi thuận nghịch!')
else:
    print('Đây không phải là chuỗi thuận nghịch!')