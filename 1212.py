while True:
    valores = input().split()
    if valores[0] == valores[1] == '0':
        break

    if len(valores[0]) > len(valores[1]):
        maior = str(int(valores[0]))
        menor = str(int(valores[1]))
    else:
        maior = str(int(valores[1]))
        menor = str(int(valores[0]))
    contador = 0
    last_carry = 0
    parou = 0
    indice_menor = len(menor) -1
    for i in range(len(maior)-1, -1,-1):
        valor = int(menor[indice_menor]) + int(maior[i])
        if valor + last_carry >= 10:
            last_carry = 1
            contador += 1
        else:
            last_carry = 0

        if indice_menor == 0:
            break
        indice_menor -=1

    if last_carry == 1:
        for d in range(len(maior) - len(menor) -1,-1,-1):
            if last_carry + int(maior[d]) >= 10:
                contador += 1
            else:
                break
    if contador > 1:
        print('{} carry operations.'.format(contador))
    elif contador == 1:
        print('1 carry operation.')
    else:
        print('No carry operation.')
        

    
        