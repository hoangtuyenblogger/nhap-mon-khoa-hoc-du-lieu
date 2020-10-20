# hàm split dùng để tách chuỗi thành các phần riêng
name = "Hoàng Kim Tuyến"
for i in name.split():
    print(i)

# hàm replace dùng để thay thế chuỗi này thành chuỗi khác
ten = "I am alone"
ten = ten.replace("alone", "not alone")
print(ten)

# hàm index trả về vị trí đầu tiên tìm thấy
print("Hàm index nè:")
print("bye bye".index('e'))
print("---------------------------------")
# hàm index trả về vị trí đầu tiên tìm thấy nhưng tìm k thấy
# thì trả về -1
print("Hàm find nè:")
print("bye bye".find('e'))
print("bye bye".find('a'))
print("---------------------------------")
# hàm upper viết hoa hết
print("Hàm upprer() nè:")
print("hoàng kim tuyến" + '-> ' +"hoàng kim tuyến".upper())
print("---------------------------------")
# hàm lower() viết thường
print("Hàm lower() nè:")
print("HOÀNG KIM TUYẾN" + '->' + "HOÀNG KIM TUYẾN".upper())
print("---------------------------------")
# hàm title() in hoa chữ cái đầu tiên của tất cả các từ
print("Hàm title() nè: nè:")
print("hoàng kim tuyến" + '->' + "hoàng kim tuyến".title())
print("---------------------------------")

