a=int(input('nhập vào số nguyên dương a='))
b=int(input('nhập vào số nguyên dương b='))
c=int(input('nhập vào số nguyên dương c='))
if (a+b>c) and (b+c>a) and (c+a>b):
    print('ba giá trị vừa nhập là một tam giác')
else:
    print('không phải là tam giác')