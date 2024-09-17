#Hàm xóa các phần tử trùng lặp trong danh sách.
def remove_duplicates(lst):
    return list(set(lst))

# Sử dụng hàm
print("Danh sách sau khi xóa phần tử trùng lặp [1, 2, 2, 3, 4, 4] là:", remove_duplicates([1, 2, 2, 3, 4, 4]))
