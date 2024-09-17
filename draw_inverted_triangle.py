#Hàm vẽ tam giác ngược với chiều cao n.
def draw_inverted_triangle(n):
    for i in range(n, 0, -1):
        print('*' * i)

# Sử dụng hàm
draw_inverted_triangle(5)
