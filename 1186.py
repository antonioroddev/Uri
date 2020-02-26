valor = input()
lista = []
for i in range(12):
    lista.append([])
    for d in range(12):
        lista[i].append(float(input()))
        
cont = 12
soma = 0
for i in range(12):
    for d in range(cont,12):
        soma += lista[d][i]
    cont -= 1

if valor == 'S':
    print(soma)
else:
    print('{:.1f}'.format(soma/66))