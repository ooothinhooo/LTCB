#Hàm tính giai thừa của một số nguyên dương.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Sử dụng hàm
print("Giai thừa của 5 là:", factorial(5))
