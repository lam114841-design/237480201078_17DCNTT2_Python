def tim_gia_tri_xa_nhat(L, x):
    """
    Hàm tìm giá trị trong list L xa x nhất.
    Xa nhất nghĩa là |giá trị - x| lớn nhất.
    """
    gia_tri_xa_nhat = L[0]
    do_lech_lon_nhat = abs(L[0] - x)

    for so in L[1:]:
        do_lech = abs(so - x)
        if do_lech > do_lech_lon_nhat:
            do_lech_lon_nhat = do_lech
            gia_tri_xa_nhat = so

    return gia_tri_xa_nhat


# --- Chạy thử ---
L = list(map(int, input("Nhập list số nguyên, cách nhau bởi dấu cách: ").split()))
x = int(input("Nhập số nguyên x: "))

ket_qua = tim_gia_tri_xa_nhat(L, x)
print("Giá trị xa x nhất là:", ket_qua)