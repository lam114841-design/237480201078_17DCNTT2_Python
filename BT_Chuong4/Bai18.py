def kiem_tra_tang_dan(L):
    """
    Hàm kiểm tra xem list L có được sắp xếp tăng dần hay không.
    Trả về True nếu đúng, False nếu không.
    """
    for i in range(len(L) - 1):
        if L[i] > L[i + 1]:
            return False
    return True


# --- Chạy thử ---
L = list(map(int, input("Nhập list số nguyên, cách nhau bởi dấu cách: ").split()))
ket_qua = kiem_tra_tang_dan(L)
print(ket_qua)