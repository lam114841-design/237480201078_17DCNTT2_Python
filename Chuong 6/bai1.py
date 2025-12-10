# sinhvien.py

class SinhVien:

    def __init__(self, ma_sv, ten_sv):
        self.ma_sv = ma_sv
        self.ten_sv = ten_sv

    def hien_thi_thong_tin(self):

        print(f"| {self.ma_sv:<10} | {self.ten_sv:<30} |")
Tạo file quanliSV.py
from sinhvien import SinhVien


class QuanLySinhVien:


    def __init__(self):
        self.danh_sach_sv = []

    # Hàm hỗ trợ tìm kiếm nội bộ
    def _tim_kiem_theo_ma(self, ma_sv):

        for sv in self.danh_sach_sv:
            if sv.ma_sv.lower() == ma_sv.lower():
                return sv
        return None

    # === CÁC CHỨC NĂNG THEO YÊU CẦU ĐỀ BÀI ===

    # 1. Thêm sinh viên
    def them_sv(self):
        ma_sv = input("   -> Nhập Mã Sinh Viên: ").strip()
        if self._tim_kiem_theo_ma(ma_sv):
            print("  Lỗi: Mã sinh viên này đã tồn tại. Thêm thất bại.")
            return

        ten_sv = input("   -> Nhập Tên Sinh Viên: ").strip()

        # Sử dụng lớp SinhVien đã import
        sinh_vien_moi = SinhVien(ma_sv, ten_sv)
        self.danh_sach_sv.append(sinh_vien_moi)
        print("  Thêm sinh viên thành công.")

    # 2. Xóa sinh viên
    def xoa_sv(self):
        ma_sv = input("   -> Nhập Mã Sinh Viên cần xóa: ").strip()
        sv_can_xoa = self._tim_kiem_theo_ma(ma_sv)

        if sv_can_xoa:
            self.danh_sach_sv.remove(sv_can_xoa)
            print(f"  Đã xóa sinh viên có Mã SV: {ma_sv}")
        else:
            print(f"  Không tìm thấy sinh viên có Mã SV: {ma_sv}")

    # 3. Sửa sinh viên (sửa tên)
    def sua_sv(self):
        ma_sv = input("   -> Nhập Mã Sinh Viên cần sửa: ").strip()
        sv_can_sua = self._tim_kiem_theo_ma(ma_sv)

        if sv_can_sua:
            ten_moi = input(f"   -> Nhập Tên mới cho SV có Mã {ma_sv}: ").strip()
            sv_can_sua.ten_sv = ten_moi
            print(f"  Sửa tên sinh viên thành công: {ten_moi}")
        else:
            print(f"  Không tìm thấy sinh viên có Mã SV: {ma_sv}")

    # 4. Tìm kiếm sinh viên
    def tim_kiem_sv(self):
        ma_sv = input("   -> Nhập Mã Sinh Viên cần tìm: ").strip()
        sv_ket_qua = self._tim_kiem_theo_ma(ma_sv)

        print("\n\t--- KẾT QUẢ TÌM KIẾM ---")
        print("\t----------------------------------------------")
        print("\t| Mã SV      | Tên Sinh Viên                |")
        print("\t----------------------------------------------")
        if sv_ket_qua:
            sv_ket_qua.hien_thi_thong_tin()
        else:
            print(f"\tKhông tìm thấy sinh viên có Mã SV: {ma_sv}")
        print("\t----------------------------------------------")

    # 5. Xem danh sách sinh viên
    def xem_danh_sach(self):
        print("\n\t===== DANH SÁCH SINH VIÊN HIỆN TẠI =====")
        if not self.danh_sach_sv:
            print("\tDanh sách hiện đang rỗng.")
            return

        print("\t----------------------------------------------")
        print("\t| Mã SV      | Tên Sinh Viên                |")
        print("\t----------------------------------------------")

        for sv in self.danh_sach_sv:
            sv.hien_thi_thong_tin()

        print("\t----------------------------------------------")

    # Chạy chương trình chính
    def menu(self):

        while True:
            print("\n\n=============== MENU CHÍNH ===============")
            print("1. Thêm sinh viên")
            print("2. Xóa sinh viên")
            print("3. Sửa sinh viên (cập nhật tên)")
            print("4. Tìm kiếm sinh viên (theo mã)")
            print("5. Xem danh sách sinh viên")
            print("0. Thoát chương trình")
            print("==========================================")

            chon = input("Chọn chức năng (0-5): ").strip()

            if chon == '1':
                self.them_sv()
            elif chon == '2':
                self.xoa_sv()
            elif chon == '3':
                self.sua_sv()
            elif chon == '4':
                self.tim_kiem_sv()
            elif chon == '5':
                self.xem_danh_sach()
            elif chon == '0':
                print("Đã thoát chương trình. Tạm biệt!")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại một số từ 0 đến 5.")


# Khởi chạy chương trình
if __name__ == "__main__":
    quan_ly = QuanLySinhVien()
    quan_ly.menu()
