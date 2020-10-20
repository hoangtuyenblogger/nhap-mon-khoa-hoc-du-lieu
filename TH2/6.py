list = []
new_list = []
n = int(input('Nhập số phần từ của list: '))
for i in range(n):
    i = int(input('NHập giá trị cho phần từ : '))
    list.append(i)
for i in list:
    so_lan_xuat_hien = list.count(i)
    if so_lan_xuat_hien == 1:
        new_list.append(i)
print('new_list = ' + str([i for i in new_list]))
