def libera(lista,tipo):
    if tipo == 'par':
        a = 'par'
    else:
        a = 'impar'
    for i in range(len(lista)):
        print('{}[{}] = {}'.format(a,i,lista.pop(0)))

lista_pares = []
lista_impares = []
for i in range(15):
    n = int(input())
    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

    if len(lista_pares) >= 5:
        libera(lista_pares,'par')
    
    if len(lista_impares) >= 5:
        libera(lista_impares,'impar')

for i in range(len(lista_impares)):
    print('impar[{}] = {}'.format(i,lista_impares.pop(0)))

for i in range(len(lista_pares)):
    print('par[{}] = {}'.format(i,lista_pares.pop(0)))