'''
list = ['cóc', 'nho', 'xoài', 'ổi']

# append thêm vào cuối
list.append('mận')
print(list)

#
list.insert(0,'dưa hấu')
print(list)
'''


# bài 1
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
so_chan = []
so_le = []
n = len(list)

print('------------- Bài 1-----------------------')
for i in range(0,n):
    if(list[i] % 2 == 0):
        so_chan.append(list[i])
    else:
        so_le.append(list[i])

for i in range(len(so_chan)):
    print('list so chan :',so_chan[i])
print('------------------------------------')
for i in range(len(so_le)):
    print('list so le :',so_le[i])



# list.pop() pop xóa phần từ cuối cùng
print('------------------------------------')
chars = ['a', 'b', 'c']
numbers = [1,2,3]
for char, number in zip(chars, numbers):
    print(char, number)

# Bài 2 | xóa phần từ khỏi list |
print('---------------Bài 2---------------------')
strings = input('Nhập vào chuỗi :')
string = strings.split(',')
string.sort()
print([i for i in string])

