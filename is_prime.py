#Hàm kiểm tra xem một số có phải là số nguyên tố hay không.
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Sử dụng hàm
print("Số 11 có phải số nguyên tố không?", is_prime(11))
print("Số 15 có phải số nguyên tố không?", is_prime(15))
