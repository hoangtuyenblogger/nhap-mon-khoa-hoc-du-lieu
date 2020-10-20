list = []

n = int(input('Nhập số phần từ của list: '))
for i in range(n):
    i = int(input('NHập giá trị cho phần từ : '))
    list.append(i)

list.sort()
dem_so_0 = list.count(0)
for i in range(dem_so_0):
    list.remove(0)
    list.append(0)
print([i for i in list])