a,b,c=eval(input('nhập vào 3 số cách bởi dấu phẩy:'))
if (a+b>c) and (a+c>b) and (b+c>a):
    if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
        print('Đây là tam giác vuông')
    elif a==b==c:
        print('Đây là tam giác đều')
    elif a==b or a==c or b==c:
        print('Đây là tam giác thường')
else:
    print('Đây không phải là tam giác')