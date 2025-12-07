def tim_sinh_vien(danh_sach, ten_can_tim):
    """
    Hàm tìm kiếm tên sinh viên trong danh sách.
    Trả về True nếu tìm thấy, False nếu không.
    """
    for ten in danh_sach:
        if ten.lower() == ten_can_tim.lower():  # so sánh không phân biệt hoa/thường
            return True
    return False


# --- Chạy thử ---
# Nhập danh sách tên sinh viên
danh_sach = input("Nhập danh sách tên sinh viên, cách nhau bởi dấu cách: ").split()

# Nhập tên cần tìm
ten_can_tim = input("Nhập tên sinh viên cần tìm: ")

# Kiểm tra
if tim_sinh_vien(danh_sach, ten_can_tim):
    print(f"Tìm thấy sinh viên '{ten_can_tim}' trong danh sách.")
else:
    print(f"Không tìm thấy sinh viên '{ten_can_tim}' trong danh sách.")
