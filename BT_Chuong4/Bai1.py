def dem_tu(chuoi):
    """
    Hàm đếm số từ trong chuỗi.
    Quy định: chuỗi chỉ có chữ cái và khoảng trắng.
    """
    # tách chuỗi theo khoảng trắng
    ds_tu = chuoi.split()
    return len(ds_tu)


# --- Chạy thử ---
chuoi = input("Nhập chuỗi: ")
so_tu = dem_tu(chuoi)
print("Số từ trong chuỗi là:", so_tu)
