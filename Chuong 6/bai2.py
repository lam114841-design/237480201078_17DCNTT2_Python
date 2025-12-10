Tạo 1 file Person.py (lớp cơ sở)
class Person:
    """
    Lớp cơ sở chứa các thông tin chung của tất cả nhân sự (Giáo viên và Học sinh).
    """

    def __init__(self, ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi):
        self.ho_ten = ho_ten
        self.gioi_tinh = gioi_tinh
        self.nam_sinh = nam_sinh
        self.noi_sinh = noi_sinh
        self.dia_chi = dia_chi

    def hien_thi_thong_tin(self):
        """Phương thức hiển thị thông tin chung."""
        print(f"- Họ tên: {self.ho_ten}, Giới tính: {self.gioi_tinh}, Năm sinh: {self.nam_sinh}")
        print(f"- Địa chỉ: {self.dia_chi} - Nơi sinh: {self.noi_sinh}")

Tạo 1 file staff.py (Các Lớp Con và Logic)
# staff.py

# Import lớp Person từ file person.py
from Person import Person


# ====================================================================
# A. Lớp GiaoVien (Kế thừa từ Person)
# ====================================================================
class GiaoVien(Person):
    """
    Lớp Giáo viên, kế thừa Person và thêm thuộc tính chuyên môn.
    """

    def __init__(self, ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi, so_nam_day, hoc_vi):
        # Gọi hàm khởi tạo của lớp cha (Person)
        super().__init__(ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi)

        # Thuộc tính riêng
        self.so_nam_day = so_nam_day
        self.hoc_vi = hoc_vi

    def hien_thi_thong_tin(self):
        print("\n--- THÔNG TIN GIÁO VIÊN ---")
        super().hien_thi_thong_tin()  # Hiển thị thông tin chung
        print(f"**CHUYÊN MÔN** -> Thâm niên: {self.so_nam_day} năm, Học vị: {self.hoc_vi}")
        print("---------------------------")


# ====================================================================
# B. Lớp HocSinh (Kế thừa từ Person)
# ====================================================================
class HocSinh(Person):
    """
    Lớp Học sinh, kế thừa Person và có logic tính điểm, xếp loại.
    """

    def __init__(self, ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi, toan, ly, hoa):
        # Gọi hàm khởi tạo của lớp cha (Person)
        super().__init__(ho_ten, gioi_tinh, nam_sinh, noi_sinh, dia_chi)

        # Thuộc tính điểm
        self.toan = toan
        self.ly = ly
        self.hoa = hoa
        self.dtb = self.tinh_dtb()
        self.xep_loai_str = self.xep_loai()

    def tinh_dtb(self):
        """Tính điểm trung bình: (Toán + Lý + Hóa) / 3"""
        if self.toan is None or self.ly is None or self.hoa is None:
            return 0.0
        return (self.toan + self.ly + self.hoa) / 3

    def xep_loai(self):
        """Xếp loại theo quy tắc đề bài."""
        dtb = self.dtb

        # Tiêu chí phụ (điểm liệt)
        diem_liet_gioi = 6.5
        diem_liet_kha = 5.0
        diem_liet_tb = 3.0

        if dtb < 5.0:
            return "Yếu"

        # Giỏi: ĐTB > 8 VÀ không môn nào dưới 6.5
        if dtb > 8.0 and self.toan >= diem_liet_gioi and self.ly >= diem_liet_gioi and self.hoa >= diem_liet_gioi:
            return "Giỏi"

        # Khá: ĐTB >= 6.5 VÀ không môn nào dưới 5
        if dtb >= 6.5 and self.toan >= diem_liet_kha and self.ly >= diem_liet_kha and self.hoa >= diem_liet_kha:
            return "Khá"

        # Trung bình: ĐTB >= 5 VÀ không môn nào dưới 3
        if dtb >= 5.0 and self.toan >= diem_liet_tb and self.ly >= diem_liet_tb and self.hoa >= diem_liet_tb:
            return "Trung bình"

        # Nếu đạt ĐTB >= 5 nhưng bị điểm liệt 3 (hoặc 5) => Trung bình (hoặc Khá, Giỏi bị hạ)
        return "Trung bình"

    def hien_thi_thong_tin(self):
        print("\n--- THÔNG TIN HỌC SINH ---")
        super().hien_thi_thong_tin()  # Hiển thị thông tin chung
        print(f"**KẾT QUẢ** -> Điểm: Toán={self.toan}, Lý={self.ly}, Hóa={self.hoa}")
        print(f"               -> ĐTB: {self.dtb:.2f} | Xếp loại: **{self.xep_loai_str}**")
        print("---------------------------")

Tạo 1 file main.py ( chạy ctrinh)
# main.py

# Import các lớp cần thiết từ file staff.py
from staff import GiaoVien, HocSinh

if __name__ == "__main__":
    print("===== DEMO QUẢN LÝ NHÂN SỰ BẰNG KẾ THỪA =====")

    ## 1. Tạo đối tượng Giáo viên
    print("\n[--- TẠO ĐỐI TƯỢNG GIÁO VIÊN ---]")
    gv_toan = GiaoVien(
        ho_ten="Nguyễn Thị Mai",
        gioi_tinh="Nữ",
        nam_sinh=1985,
        noi_sinh="Hà Tĩnh",
        dia_chi="Đường ABC, Hà Nội",
        so_nam_day=18,
        hoc_vi="Thạc sĩ"
    )

    ## 2. Tạo các đối tượng Học sinh
    print("\n[--- TẠO CÁC ĐỐI TƯỢNG HỌC SINH ---]")

    # Học sinh Giỏi: ĐTB > 8 và không môn nào dưới 6.5
    hs_gioi = HocSinh("Trần Minh Đức", "Nam", 2008, "TP.HCM", "Quận 10", 9.5, 9.0, 9.2)

    # Học sinh Khá: ĐTB >= 6.5 và không môn nào dưới 5
    hs_kha = HocSinh("Phạm Thanh Vân", "Nữ", 2007, "Đà Nẵng", "Quận Hải Châu", 7.0, 6.0, 6.5)

    # Học sinh Trung bình (bị điểm liệt Khá: ĐTB cao nhưng môn Lý dưới 5)
    hs_tb1 = HocSinh("Võ Hoài Nam", "Nam", 2008, "Hà Nội", "Đống Đa", 9.0, 4.0,
                     8.0)  # ĐTB 7.0, nhưng Lý < 5.0 -> Xếp TB

    # Học sinh Yếu: ĐTB < 5
    hs_yeu = HocSinh("Đặng Thu Phương", "Nữ", 2007, "Cần Thơ", "Ninh Kiều", 4.0, 4.5, 3.5)

    print("\n\n=============== KẾT QUẢ HIỂN THỊ ===============")

    # Hiển thị thông tin
    gv_toan.hien_thi_thong_tin()
    hs_gioi.hien_thi_thong_tin()
    hs_kha.hien_thi_thong_tin()
    hs_tb1.hien_thi_thong_tin()
    hs_yeu.hien_thi_thong_tin()
    print("==================================================")

