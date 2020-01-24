n = int(input())

for i in range(n):
    lista = input().split()

    somador = 0
    for valor in lista[1:]:
        somador += int(valor)

    media_total = somador / int(lista[0])
    contador = 0
    for valor in lista[1:]:
        if int(valor) > (media_total):
            contador +=1

    print("{:.3f}%" .format(100 * (contador/ int(lista[0]))))