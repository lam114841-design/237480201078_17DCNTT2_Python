van=float(input('nhap diem van= '))
toan=float(input('nhap diem toan= '))
anh=float(input('nhap diem anh= '))
tb=(van+toan+anh)/3
print(f"Điểm trung bình: {tb:.2f}")
if tb >=8.5 and toan>=9 and toan>van and toan>anh:
    print('Đậu chuyên Toán')
elif tb >=8.5 and van>=9 and van>= anh:
    print('Đậu chuyên Văn')
elif tb >=8.5 and anh >=8.0:
    print('Đậu chuyên Anh')
elif tb >=8.5:
    print('Đậu chuyên Tin Học')
else:
    print('Học sinh không đậu chuyên')