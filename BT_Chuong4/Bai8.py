def kiem_tra_mat_khau_manh(mat_khau):
    """
    Kiểm tra mật khẩu mạnh theo các tiêu chí:
    - Ít nhất 1 ký tự đặc biệt
    - Ít nhất 1 ký tự in hoa
    - Ít nhất 1 ký tự số
    - Ít nhất 1 ký tự in thường
    - Độ dài > 6
    """
    co_in_hoa = False
    co_in_thuong = False
    co_chu_so = False
    co_dac_biet = False

    if len(mat_khau) <= 6:
        return False

    for ky_tu in mat_khau:
        if ky_tu.isupper():
            co_in_hoa = True
        elif ky_tu.islower():
            co_in_thuong = True
        elif ky_tu.isdigit():
            co_chu_so = True
        else:
            co_dac_biet = True

    return co_in_hoa and co_in_thuong and co_chu_so and co_dac_biet


# --- Chạy thử ---
chuoi_nhap = input("Nhập mật khẩu: ")
if kiem_tra_mat_khau_manh(chuoi_nhap):
    print("Đây là mật khẩu mạnh")
else:
    print("Mật khẩu chưa đủ mạnh")