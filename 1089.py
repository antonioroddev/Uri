valor = input()
lista = []

TAM  = 12
for i in range(TAM):
    lista.append([])
    for d in range(TAM):
        lista[i].append(float(input()))
        
cont1 = 6
cont2 = 6
soma = 0
for i in range(5,-1,-1):
    for d in range(cont1,cont2):
        soma += lista[d][i]
    cont1 -= 1
    cont2 += 1

if valor == 'S':
    print(soma)
else:
    print('{:.1f}'.format(soma/66))