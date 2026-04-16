#máy tính điện tử
def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        print("Lỗi chia cho 0")
    else:
        return a / b

def hien_thi_menu():
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")

while True:
    hien_thi_menu()
    chon = int(input("Chọn: "))

    if chon == 5:
        break

    if chon in [1, 2, 3, 4]:
        a = float(input("Nhập a: "))
        b = float(input("Nhập b: "))

        if chon == 1:
            print("Kết quả:", cong(a, b))
        elif chon == 2:
            print("Kết quả:", tru(a, b))
        elif chon == 3:
            print("Kết quả:", nhan(a, b))
        elif chon == 4:
            print("Kết quả:", chia(a, b))