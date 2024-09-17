#Hàm vẽ tam giác vuông với cạnh dài n.
def draw_right_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

# Sử dụng hàm
draw_right_triangle(5)
