#Hàm kiểm tra xem một số có phải là số chẵn hay không.
def is_even(number):
    return number % 2 == 0

# Sử dụng hàm
print("Số 4 có phải số chẵn không?", is_even(4))
print("Số 7 có phải số chẵn không?", is_even(7))
