#Hàm vẽ hình chóp với chiều cao n.
def draw_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# Sử dụng hàm
draw_pyramid(5)
