def vi_tri_max(L):
    max_value = max(L)
    return L.index(max_value)

L = list(map(int, input("Nhập list số nguyên (cách nhau dấu cách): ").split()))
print("Vị trí giá trị lớn nhất:", vi_tri_max(L))