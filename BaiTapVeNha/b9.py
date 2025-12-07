tien = int(input("Nhập số tiền: "))
menh_gia = [50000, 20000, 10000, 5000, 2000, 1000]

print("Tổng cộng là:")
for mg in menh_gia:
    so_to, tien = divmod(tien, mg)  #divmod(a, b)
    if so_to:
        print(f"{mg} đồng: {so_to} tờ")

''' divmod(a,n) -> trả về một tuple gồm 2 giá trị:
    Thương → a // b
    Số dư  → a % b ( a: số bị chia (dividend)
                     b: số chia     (divisor) )'''