#Hàm vẽ hình thoi với chiều cao n (phải là số lẻ).


def draw_diamond(n):
    if n % 2 == 0:
        print("Chiều cao phải là số lẻ.")
        return
    
    # Vẽ nửa trên
    for i in range(n // 2 + 1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
    
    # Vẽ nửa dưới
    for i in range(n // 2 - 1, -1, -1):
        print(' ' * (n // 2 - i) + '*' * (2 * i + 1))

# Sử dụng hàm
draw_diamond(7)
