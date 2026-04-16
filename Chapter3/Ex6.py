#Dự án quản lý danh bạ
def add_contact(danh_ba):
    ten = input("Nhập tên: ")
    sdt = input("Nhập SĐT: ")
    danh_ba.append(ten + " - " + sdt)
    print("Thêm thành công")

def show_contacts(danh_ba):
    if not danh_ba:
        print("Chưa có liên hệ nào")
    else:
        for i in range(len(danh_ba)):
            print(i + 1, ".", danh_ba[i])

def search_contact(danh_ba):
    ten = input("Nhập tên cần tìm: ")
    found = False
    for contact in danh_ba:
        if ten in contact:
            print(contact)
            found = True
    if not found:
        print("Không tìm thấy")

def main():
    my_contacts = []

    while True:
        print("=== HỆ THỐNG QUẢN LÝ DANH BẠ ===")
        print("1. Thêm liên hệ mới")
        print("2. Hiển thị tất cả danh bạ")
        print("3. Tìm kiếm liên hệ")
        print("4. Thoát")
        chon = int(input("Chọn: "))

        if chon == 1:
            add_contact(my_contacts)
        elif chon == 2:
            show_contacts(my_contacts)
        elif chon == 3:
            search_contact(my_contacts)
        elif chon == 4:
            break

main()