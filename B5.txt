import math

# Nhập bán kính từ người dùng
radius = float(input("Nhập bán kính của hình tròn: "))

if radius < 0:
    print("Bán kính không thể là số âm. Vui lòng nhập lại.")
    exit()  # Kết thúc chương trình khi bán kính không hợp lệ

# Tính chu vi và diện tích
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# In kết quả ra màn hình
print(f"Chu vi của hình tròn là: {circumference:.2f}")
print(f"Diện tích của hình tròn là: {area:.2f}")


#---------------------------------------------------

import math
 # Nhập độ dài ba cạnh của tam giác
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

# Kiểm tra xem ba cạnh có phải là cạnh của một tam giác hợp lệ không
if a <= 0 or b <= 0 or c <= 0:
    print("Độ dài các cạnh phải là số dương. Vui lòng nhập lại.")
    exit()

if a + b <= c or a + c <= b or b + c <= a:
    print("Ba cạnh không thể tạo thành một tam giác hợp lệ.")
    exit()

# Tính chu vi
perimeter = a + b + c

# Tính diện tích bằng công thức Heron
s = perimeter / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# In kết quả ra màn hình
print(f"Chu vi của hình tam giác là: {perimeter:.2f}")
print(f"Diện tích của hình tam giác là: {area:.2f}")


#---------------------------------------------------
