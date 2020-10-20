'''
tuple_cua_tui = ('chanh','cóc','xoài', 'ổi')
print(tuple_cua_tui)

tuple_1_thanh_phan = ('chanh',)
print(tuple_1_thanh_phan)

'''
tuple1 = tuple(('chanh','cóc','xoài', 'ổi'))

'''
list_ne = list(tuple1)
print(list_ne)

list_ne[0] = 'cà chua'
tuple1 = tuple(list_ne)
print(tuple1)

for i in tuple1:
    print(i)

if 'cà chua' in tuple1:
    print('có cà chua trong tuple')


tuple2 = ('3','2','1')

tuple3 = ('4','5','6')
tuple4 = tuple2 + tuple3
print(tuple4)

print(tuple4.index('3')) # vị trí của phần từ '3'
'''

########## SET : các giá trị trong set là duy nhất
my_set = {'1', '2','4'}



my_set.remove('1')
my_set.pop()
print(type(my_set))

#my_set.clear()
my_set.add('3')
my_set.update('5','10')
print(my_set)
