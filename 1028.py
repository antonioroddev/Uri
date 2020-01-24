def mdc_rec(maior,menor):
    if maior == menor:
        print(menor)
    elif (maior % menor) == 0:
        print(menor)
    else:
        r = maior % menor
        if (r == 0):
            print(maior)
        else:
            mdc_rec(menor,r)


n = int(input())

for i in range(n):
    lista = input().split()

    if int(lista[0]) > int(lista[1]):
        maior = int(lista[0])
        menor = int(lista[1])
    else:
        maior = int(lista[1])
        menor = int(lista[0])

    mdc_rec(maior,menor)