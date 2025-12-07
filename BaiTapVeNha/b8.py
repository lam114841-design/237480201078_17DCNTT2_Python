n=int(input('nhập vào số nguyên có 4 chữ số = '))
a = n // 1000
b = (n // 100) % 10
c = (n // 10) % 10
d = n % 10
tong = a+b+c+d
print('Tổng các chữ số nguyên vừa nhập là:',tong)

#dùng chuỗi
'''n = input("Nhập vào số nguyên có 4 chữ số: ")
tong = sum(int(chuso) for chuso in n)
print("Tổng các chữ số của", n, "là:", tong)
'''