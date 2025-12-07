a=int(input('nhập a='))
b=int(input('nhap b='))
if (a<b):
    uc=a
else:
    uc=b
while ( a%uc!=0) or (b%uc!=0):
    uc=uc-1
print('USCLN(',a,',',b,') =',uc)
