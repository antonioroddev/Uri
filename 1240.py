n = int(input())

for i in range(n):
    lista = input().split()
    if len(lista[1]) > len(lista[0]):
        print("nao encaixa")
    else:
        if lista[0][-len(lista[1]):] == lista[1]:
            print("encaixa")
        else:
            print('nao encaixa') 