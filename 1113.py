while True:
   
    lista = [int (i) for i in input().split()]
    if lista[0] > lista[1]:
        print('Decrescente')
    elif lista[0] < lista[1]:
        print('Crescente')
    else:
        break
