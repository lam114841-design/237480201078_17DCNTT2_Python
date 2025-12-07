n=int(input('Nhập số nguyên dương:'))
while n<=0:
    n = int(input('Nhập lại số nguyên dương:'))
s=i=0
while True:
    i=i+1
    s=s+i
    if s>=n:
        i=i-1
        break
print('k=',i)