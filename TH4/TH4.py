def a_mu_n(a,n):
    return a ** n
def kt_chan_le(a):
    if a < 0:
        return False
    elif a % 2 == 0:
        return True
    else:
        return False
def sont(a):
    from math import sqrt
    if a < 0:
        return False
    elif a == 2:
        return True
    else:
        for i in range(2,sqrt(a),1):
            if a % 2 == 0:
                return False
        return True
def day_sont(n):
    for i in range(n+1):
        if sont(i):
            print(i)
def dtich_htron(r):
    return 3.14 * r * r * 1.0
def ucln(a,b):
    if b ==0:
        return a
    else:
        return ucln(b,a%b)
def bangcuuchuong(n):
    for i in range(1,10,1):
        print(n,"x",i,"=",i*n)

bangcuuchuong(2)