while True:

    try:

        lista = input()
        lista = lista.replace('=','+')
        lista = lista.split('+')
        lista_letras = ['R','L','J']
        if lista[0] in lista_letras:
            print(int(lista[2]) - int(lista[1]))
        elif lista[1] in lista_letras:
            print(int(lista[2]) - int(lista[0]))
        else:
            print(int(lista[0]) + int(lista[1]))


    except EOFError:
        break