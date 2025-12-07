def tong_cac_so_trong_chuoi(chuoi):
    """
    Hàm tách toàn bộ ký tự số trong chuỗi và tính tổng của chúng.
    """
    tong = 0
    cac_so = []

    for ky_tu in chuoi:
        if ky_tu.isdigit():       # kiểm tra ký tự có phải số
            gia_tri = int(ky_tu)  # chuyển ký tự số thành số nguyên
            cac_so.append(gia_tri)
            tong += gia_tri

    return cac_so, tong


# --- Chạy thử ---
chuoi_nhap = input("Nhập vào một chuỗi: ")
cac_so, tong = tong_cac_so_trong_chuoi(chuoi_nhap)

print("Các ký tự số tách ra:", cac_so)
print("Tổng các số:", tong)