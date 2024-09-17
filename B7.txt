#-------------------------------------------------

#In bảng cửu chương của số nhập vào

number = int(input("Nhập một số để in bảng cửu chương: "))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")



#-------------------------------------------------

def print_star_triangle():
    rows = int(input("Nhập số hàng của hình tam giác sao: "))
    for i in range(1, rows + 1):
        print('*' * i)

if __name__ == "__main__":
    print_star_triangle()

#-------------------------------------------------
correct_password = "password123"
while True:
    entered_password = input("Nhập mật khẩu: ")
    if entered_password == correct_password:
        print("Mật khẩu đúng!")
        break
    else:
        print("Mật khẩu sai, vui lòng thử lại.")




#-------------------------------------------------


#-------------------------------------------------


#-------------------------------------------------
