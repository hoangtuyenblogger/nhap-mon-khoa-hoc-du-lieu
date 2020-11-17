# bài 1 hàm tính n!
def giaithua(n):
    gt = 1
    if n < 0:
        return -1
    if n == 0:
        return 1
    else:
        for i in range(1,n+1,1):
            gt *= i
        return gt

def tong(n):
    s= 0
    for i in range(1,n+1,1):
        s +=i
    return s

if __name__ == '__main__':
    print(giaithua(3))
    print(tong(3))