def chuoi_ngan_nhat(L):
    return min(L, key=len)

L = input("Nhập các chuỗi cách nhau dấu cách: ").split()
print("Chuỗi ngắn nhất là:", chuoi_ngan_nhat(L))
