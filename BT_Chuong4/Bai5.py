def dem_ky_tu(chuoi):
    """
    Hàm đếm số ký tự in hoa, in thường và số trong chuỗi.
    """
    so_in_hoa = 0
    so_in_thuong = 0
    so_chu_so = 0

    for ky_tu in chuoi:
        if ky_tu.isupper():       # ký tự in hoa
            so_in_hoa += 1
        elif ky_tu.islower():     # ký tự in thường
            so_in_thuong += 1
        elif ky_tu.isdigit():     # ký tự số
            so_chu_so += 1

    return so_in_hoa, so_in_thuong, so_chu_so


# --- Chạy thử ---
chuoi_nhap = input("Nhập vào một chuỗi: ")
hoa, thuong, so = dem_ky_tu(chuoi_nhap)

print("Số ký tự in hoa:", hoa)
print("Số ký tự in thường:", thuong)
print("Số ký tự số:", so)