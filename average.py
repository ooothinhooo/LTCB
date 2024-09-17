#Hàm tính trung bình cộng của các số trong danh sách.
def average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Sử dụng hàm
print("Trung bình cộng của danh sách [4, 5, 6, 7] là:", average([4, 5, 6, 7]))
