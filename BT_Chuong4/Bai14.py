def tim_so_duong_dau_tien(L):
    """
    Hàm tìm số dương đầu tiên trong list L.
    Nếu không có thì trả về -1.
    """
    for x in L:
        if x > 0:
            return x
    return -1


# --- Chạy thử ---
L = list(map(int, input("Nhập list số nguyên, cách nhau bởi dấu cách: ").split()))
ket_qua = tim_so_duong_dau_tien(L)
print("Số dương đầu tiên là:", ket_qua)