# main.py

from manager import QuanLySinhVien

ql = QuanLySinhVien()

while True:
    print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
    print("1. Thêm sinh viên")
    print("2. Hiển thị danh sách")
    print("3. Tìm sinh viên theo mã")
    print("4. Xóa sinh viên")
    print("5. Cập nhật sinh viên")
    print("6. Thoát")

    chon = input("Nhập lựa chọn: ")

    if chon == "1":
        ql.them_sv()
    elif chon == "2":
        ql.hien_thi()
    elif chon == "3":
        ql.tim_sv()
    elif chon == "4":
        ql.xoa_sv()
    elif chon == "5":
        ql.cap_nhat_sv()
    elif chon == "6":
        print("Thoát chương trình...")
        break
    else:
        print("Lựa chọn không hợp lệ!")
