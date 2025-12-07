n=int(input('nhap vao so nguyen duong= '))

chan =0
le=0
for ch in str(n):     # ch : ký tự
    so=int(ch)

    if so %2==0:
        chan +=1
    else:
        le +=1

print("Số", n, "có", chan, "chữ số chẵn và", le, "chữ số lẻ")

