n=int(input('nhap vao so nguyen duong n= '))
#dùng hàm sum() and range()
print("Tổng các số lẻ nhỏ hơn", n, "là:", sum(range(1, n, 2))) #sart 1 - bước nhảy 2 : lẻ
print("Tổng các số chẵn nhỏ hơn", n, "là:", sum(range(0, n, 2)))