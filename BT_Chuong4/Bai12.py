def tim_nho_nhat(L, a, b):
    """
    Hàm tìm số nhỏ nhất trong list L
    từ vị trí a đến vị trí b (bao gồm cả a và b).
    """
    # cắt list từ a đến b
    doan = L[a:b+1]

    # duyệt để tìm số nhỏ nhất (không dùng min)
    nho_nhat = doan[0]
    for x in doan[1:]:
        if x < nho_nhat:
            nho_nhat = x

    return nho_nhat


# --- Chạy thử ---
L = [10, 3, 25, 7, 2, 15, 8]
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

if 0 <= a < b < len(L):
    ket_qua = tim_nho_nhat(L, a, b)
    print(f"Số nhỏ nhất từ vị trí {a} đến {b} là:", ket_qua)
else:
    print("Giá trị a, b không hợp lệ!")