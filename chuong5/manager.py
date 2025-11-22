# manager.py

from student import SinhVien

class QuanLySinhVien:
    def __init__(self):
        self.ds = []

    def them_sv(self):
        ma = input("Nhập mã sinh viên: ")
        ten = input("Nhập tên sinh viên: ")
        tuoi = input("Nhập tuổi: ")
        lop = input("Nhập lớp: ")

        sv = SinhVien(ma, ten, tuoi, lop)
        self.ds.append(sv)
        print("=> Thêm sinh viên thành công!")

    def hien_thi(self):
        if not self.ds:
            print("Danh sách sinh viên trống!")
            return
        print("\n===== DANH SÁCH SINH VIÊN =====")
        for sv in self.ds:
            print(sv)

    def tim_sv(self):
        ma = input("Nhập mã sinh viên cần tìm: ")
        for sv in self.ds:
            if sv.ma == ma:
                print("=> Tìm thấy sinh viên:")
                print(sv)
                return
        print("=> Không tìm thấy!")

    def xoa_sv(self):
        ma = input("Nhập mã sinh viên cần xóa: ")
        for sv in self.ds:
            if sv.ma == ma:
                self.ds.remove(sv)
                print("=> Xóa sinh viên thành công!")
                return
        print("=> Không tìm thấy sinh viên để xóa!")

    def cap_nhat_sv(self):
        ma = input("Nhập mã sinh viên cần cập nhật: ")
        for sv in self.ds:
            if sv.ma == ma:
                print("Nhập thông tin mới (bỏ trống nếu không đổi):")
                ten = input(f"Tên ({sv.ten}): ") or sv.ten
                tuoi = input(f"Tuổi ({sv.tuoi}): ") or sv.tuoi
                lop = input(f"Lớp ({sv.lop}): ") or sv.lop

                sv.ten = ten
                sv.tuoi = tuoi
                sv.lop = lop
                print("=> Cập nhật thành công!")
                return
        print("=> Không tìm thấy sinh viên để cập nhật!")
