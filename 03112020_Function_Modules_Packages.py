from math import sqrt
# giải pt bậc 1
def ptbac1(a, b):
    if a == 0 and b > 0:
        print("Vô nghiệm")
        return -99999999

    return float(-b/a)

 # pt bậc 2
def giaiptbac2(a,b,c):
     if a == 0:
         if b == 0:
             if c == 0:
                 print("Phương trình vô số nghiệm!")
             else:
                 print("Phương trình vô nghiệm!")
         else:
             if c == 0:
                 print("Phương trình có 1 nghiệm x = 0")
             else:
                 print("Phương trình có 1 nghiệm x = ", -c / b)
     else:
         delta = b ** 2 - 4 * a * c
         if delta < 0:
             print("Phương trình vô nghiệm!")
         elif delta == 0:
             print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
         else:
             print("Phương trình có 2 nghiệm phân biệt!")
             print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
             print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))
a = list(input("Nhập chuỗi 1:").split(' '))
b = input("Nhập chuỗi 2:").split(' ')

for i in a:
    print(i)

