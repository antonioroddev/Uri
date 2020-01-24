from math import sqrt
while True:
    try:
        lista = input().split()
        a,b,c = int(lista[0]),int(lista[1]),int(lista[2])
        reta3 = (sqrt(a*a+ 12*12))
        
        if 12/b < reta3/c:
            print('N')
        else:
            print('S')

    except EOFError:
        break