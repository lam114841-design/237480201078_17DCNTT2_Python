i=0
for g in range(1,100):
    for c in range(1,100-g):
        if ( g+c==36 and g*2+c*4==100):
            i=i+1
            print('Cach',i,': Voi so ga la:',g,'Va so cho la:',c)