while True:

    lista = input()

    if lista == '0+0=0':
        print('True')
        break
    
    lista = lista.replace('=','+')
    lista = lista.split('+')
    
    comp0 = lista[0][::-1]
    comp1 = lista[1][::-1]
    comp2 = lista[2][::-1]

    if int(comp0) + int(comp1) == int(comp2):
        print('True')

    else:
        print('False')


