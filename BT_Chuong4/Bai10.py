def xoa_chuoi(a, b):
    """
    Hàm xóa toàn bộ chuỗi b trong chuỗi a
    mà không dùng hàm replace()
    """
    ket_qua = ""
    i = 0
    while i < len(a):
        # nếu tại vị trí i bắt đầu bằng b
        if a[i:i+len(b)] == b:
            i += len(b)  # bỏ qua đoạn b
        else:
            ket_qua += a[i]
            i += 1
    return ket_qua


# --- Chạy thử ---
chuoi_a = input("Nhập chuỗi a: ")
chuoi_b = input("Nhập chuỗi b: ")

ket_qua = xoa_chuoi(chuoi_a, chuoi_b)
print("Chuỗi sau khi xóa:", ket_qua)