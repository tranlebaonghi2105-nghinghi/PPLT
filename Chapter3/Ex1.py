#Tính toán cơ bản và rẽ nhánh
km =float(input("Nhập số ki-lô-mét (km) cần tính:"))

if km <= 1:
    tien = 15000
elif km <= 20:
    tien = 15000 + (km - 1) * 12000
else:
    tien = 15000 + 19 * 12000 + (km - 20) * 10000

print("Số tiền phải trả:", tien, "VNĐ")