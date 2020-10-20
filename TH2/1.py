import math
def songuyento(n):
    # so nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;

    # check so nguyen to khi n >= 2
    k = int(math.sqrt(n));
    for i in range(2, k + 1):
        if (n % i == 0):
            return False;
    return True;

list_nguyen_to = []
n = int(input('Nhập vào số n :'))
for i in range(1,n+1):
    if songuyento(i) == True:
        list_nguyen_to.append(i)
for i in list_nguyen_to:
    print(i)
