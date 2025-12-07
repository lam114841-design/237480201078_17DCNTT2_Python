def la_list_chan_le(L):
    """
    Kiểm tra list L có phải là list chẵn lẻ hay không.
    """
    so_chan = sum(1 for x in L if x % 2 == 0)
    so_le = len(L) - so_chan

    # Điều kiện: phải có ít nhất 1 số chẵn và 1 số lẻ
    # và không được có nhiều hơn 1 số cùng loại
    return (so_chan == 1 and so_le >= 1) or (so_le == 1 and so_chan >= 1)


# --- Chạy thử ---
L = list(map(int, input("Nhập list số nguyên, cách nhau bởi dấu cách: ").split()))
if la_list_chan_le(L):
    print("True")
else:
    print("False")