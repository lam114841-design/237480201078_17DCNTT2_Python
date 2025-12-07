def tim_vi_tri(L):
    """
    Hàm tìm vị trí trong list L thỏa:
    - Có 2 giá trị lân cận
    - Giá trị tại vị trí đó = tích 2 giá trị lân cận
    Nếu không có thì trả về -1
    """
    for i in range(1, len(L) - 1):  # duyệt từ phần tử thứ 2 đến áp chót
        if L[i] == L[i-1] * L[i+1]:
            return i
    return -1


# --- Chạy thử ---
L = list(map(int, input("Nhập list số nguyên, cách nhau bởi dấu cách: ").split()))
vi_tri = tim_vi_tri(L)
print("Vị trí tìm được:", vi_tri)