#Hàm vẽ hình X với kích thước n (phải là số lẻ).
def draw_x(n):
    if n % 2 == 0:
        print("Kích thước phải là số lẻ.")
        return

    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# Sử dụng hàm
draw_x(5)
