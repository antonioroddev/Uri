n = int(input())

for i in range(n):
    contador = 0
    valor = input()

    for letra in valor:
        if int(letra) == 0:
            contador += 6
        elif int(letra) == 1:
            contador += 2
        elif int(letra) == 2:
            contador += 5
        elif int(letra) == 3:
            contador += 5
        elif int(letra) == 4:
            contador += 4
        elif int(letra) == 5:
            contador += 5
        elif int(letra) == 6:
            contador += 6
        elif int(letra) == 7:
            contador += 3
        elif int(letra) == 8:
            contador += 7
        elif int(letra) == 9:
            contador += 6
        

    print('{} leds'.format(contador))