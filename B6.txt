year = int(input("Nhập một năm: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Năm {year} là năm nhuận.")
else:
    print(f"Năm {year} không phải là năm nhuận.")


#-------------------------------------------------
a = float(input("Nhập độ dài cạnh a: "))
b = float(input("Nhập độ dài cạnh b: "))
c = float(input("Nhập độ dài cạnh c: "))

if a == b == c:
    print("Đây là tam giác đều.")
elif a == b or b == c or a == c:
    print("Đây là tam giác cân.")
else:
    print("Đây là tam giác thường.")


#-------------------------------------------------


weight = float(input("Nhập trọng lượng gói hàng (kg): "))
if weight <= 1:
    cost = 5
elif weight <= 5:
    cost = 10
elif weight <= 10:
    cost = 20
else:
    cost = 50
print(f"Phí vận chuyển cho gói hàng {weight} kg là ${cost}.")


#-------------------------------------------------



score = float(input("Nhập điểm của học sinh (0-10): "))
if score >= 9:
    print("Điểm của bạn là xuất sắc.")
elif score >= 7:
    print("Điểm của bạn là giỏi.")
elif score >= 5:
    print("Điểm của bạn là khá.")
elif score >= 3:
    print("Điểm của bạn là trung bình.")
else:
    print("Điểm của bạn là yếu.")

#-------------------------------------------------

weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (m): "))
bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Gầy"
elif bmi < 24.9:
    category = "Bình thường"
elif bmi < 29.9:
    category = "Thừa cân"
else:
    category = "Béo phì"

print(f"Chỉ số BMI của bạn là {bmi:.2f}. Bạn thuộc diện {category}.")