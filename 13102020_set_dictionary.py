tdmu = {"name" : "Dai hoc Thu Dau Mot",
        "address": "06 Tran Van On"}



tdmu["class"] = "d18ht01"
tdmu["class2"] = "d18ht02"

print(tdmu)

#tdmu.pop("class2")
#print("tdmu pop :", tdmu)

tdmu.popitem()
print("tdmu pop item :", tdmu)


print(type(tdmu))

d18ht01 = dict(siso = 32, loptruong = "Quoc Dung")
print(d18ht01)

# Bài 1
''' Viết chương trình nhập vào số điện thoại, in ra số điện thoại ở dạng kí tự'''
sdt =  {
    "0" : "không",
    "1" : "một",
    "2" : "hai",
    "3" : "ba",
    "4" : "bốn",
    "5": "năm",
    "6": "sáu",
    "7": "bảy",
    "8": "tám",
    "9": "chín",
}
sdt_string = ""
sdt_ne = input("Nhập số điện thoại của bạn : ")

for i in sdt_ne:
    sdt_string += sdt.get(i) + " "
print("Số điện thoại của bạn là : ",sdt_string)


# bài 2
n = int(input("Nhập n = "))
my_dict = {}
for i in range(1,n+1):
    my_dict[i]= i*i
print(my_dict)