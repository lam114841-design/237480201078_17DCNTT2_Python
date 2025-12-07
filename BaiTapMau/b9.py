'''a,b,c=eval(input('nhập vào 3 số cách bởi dấu phẩy:'))
if (a>b):
    if (a>c):
        if (b>c):
            print('c,b,a') #a>b>c
        else:
            print(b,c,a) #b<c<a
    else:
        print(b,a,c) #b<a<c
else:  #a<b
    if(b>c):
        if(a>c):
            print(c,a,b) #c<a<b
        else:
            print(a,c,b) #a<c<b
    else:
        print(a,b,c) #a<b<c'''


a,b,c=eval(input('nhập vào 3 số cách bởi dấu phẩy:'))    #cách này nhanh hơn
print(*sorted([a,b,c]))                                  #dùng để sắp xếp tt
