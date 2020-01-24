contador = 1
while True:
    lista = input().split()
    if lista[0] == lista[1] == '0':
        break

    if int(lista[0]) > (26 * int(lista[1])) + int(lista[1]):
        print("Case {}: impossible" .format(contador))
    else:
        valor = 0
        if int(lista[0]) <= int(lista[1]):
            print("Case {}: 0" .format(contador))
        else:
            while True:
                if (valor * int(lista[1])) + int(lista[1]) >= int(lista[0]):
                    break
                valor += 1
            print("Case {}: {}" .format(contador,valor))

    contador += 1
