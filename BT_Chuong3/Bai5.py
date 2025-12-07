def tim_vi_tri_k(L, k):
    for i in range(len(L)):
        if L[i] == k:
            return i
    return -1

L = list(map(int, input("Nhập list số nguyên: ").split()))
k = int(input("Nhập số nguyên k: "))
print("Vị trí của k:", tim_vi_tri_k(L, k))
